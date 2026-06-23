import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Laptop Recommendation System",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Laptop Recommendation System")

# Load Dataset
data = pd.read_csv("recommendation_data.csv")

# Usage
usage = st.selectbox(
    "Select Usage",
    [
        "Gaming",
        "Programming",
        "Design",
        "Office",
        "Student"
    ]
)

# Budget
budget = st.number_input(
    "Enter Budget (EGP)",
    min_value=5000,
    step=1000
)

def recommend_laptops(data, usage, budget):

    if usage == "Gaming":
        filtered = data[
            (data["GPU_Score"] >= 3) &
            (data["ram(GB)"] >= 16) &
            (data["price"] <= budget) &
            (data["CPU_Class"] >= 3)
        ]

    elif usage == "Programming":
        filtered = data[
            (data["CPU_Class"] >= 3) &
            (data["ram(GB)"] >= 8) &
            (data["ssd(GB)"] >= 512) &
            (data["price"] <= budget)
        ]

    elif usage == "Design":
        filtered = data[
            (data["GPU_Score"] >= 3) &
            (data["VRAM_GB"] >= 4) &
            (data["ram(GB)"] >= 16) &
            (data["price"] <= budget)
        ]

    elif usage == "Office":
        filtered = data[
            (data["ram(GB)"] >= 8) &
            (data["price"] <= budget)
        ]

    else:
        filtered = data[
            (data["ram(GB)"] >= 8) &
            (data["price"] <= budget)
        ]

    if not filtered.empty:

        filtered = filtered.sort_values(
            by=["CPU_Class", "GPU_Score", "ram(GB)", "ssd(GB)"],
            ascending=False
        )

        return filtered[[
            "model_name",
            "brand",
            "processor_name",
            "graphics",
            "ram(GB)",
            "ssd(GB)",
            "price",
            "Category"
        ]].head(10)

    else:

        alternatives = data[
            data["price"] <= budget * 1.2
        ]

        alternatives = alternatives.sort_values(
            by=["CPU_Class", "GPU_Score", "ram(GB)"],
            ascending=False
        )

        return alternatives[[
            "model_name",
            "brand",
            "processor_name",
            "graphics",
            "ram(GB)",
            "ssd(GB)",
            "price",
            "Category"
        ]].head(10)

if st.button("Recommend Laptops 🎯"):

    results = recommend_laptops(
        data,
        usage,
        budget
    )

    results = results.reset_index(drop=True)

    for i, row in results.iterrows():

        st.markdown("---")

        st.subheader(f"💻 {row['model_name']}")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Brand:** {row['brand']}")
            st.write(f"**Processor:** {row['processor_name']}")
            st.write(f"**Graphics:** {row['graphics']}")

        with col2:
            st.write(f"**RAM:** {row['ram(GB)']} GB")
            st.write(f"**SSD:** {row['ssd(GB)']} GB")
            st.write(f"**Category:** {row['Category']}")

        st.success(
            f"Price: {row['price']:,} EGP"
        )