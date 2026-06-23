import streamlit as st
import pandas as pd

# =====================================
# Page Config
# =====================================

st.set_page_config(
    page_title="Smart Laptop Advisor",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Smart Laptop Advisor")
st.subheader("Laptop Price Prediction System")

# =====================================
# Brands
# =====================================

brands = [
    "AGB", "Acer", "Apple", "Asus", "Avita",
    "Chuwi", "Dell", "Fujitsu", "Gigabyte",
    "HP", "Honor", "Huawei", "Infinix",
    "LG", "Lenovo", "MSI", "Microsoft",
    "Nokia", "Realme", "Samsung",
    "Ultimus", "Xiaomi"
]

# =====================================
# Operating Systems
# =====================================

operating_systems = [
    "Windows",
    "DOS",
    "Ubuntu",
    "Mac",
    "Chrome"
]

# =====================================
# Layout
# =====================================

col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox(
        "Select Brand",
        brands
    )

with col2:
    os_name = st.selectbox(
        "Operating System",
        operating_systems
    )

# =====================================
# RAM
# =====================================

ram = st.selectbox(
    "RAM (GB)",
    [4, 8, 12, 16, 32, 64]
)

# =====================================
# Create Input DataFrame
# =====================================

columns = [
    'brand_AGB', 'brand_Acer', 'brand_Apple',
    'brand_Asus', 'brand_Avita', 'brand_Chuwi',
    'brand_Dell', 'brand_Fujitsu', 'brand_Gigabyte',
    'brand_HP', 'brand_Honor', 'brand_Huawei',
    'brand_Infinix', 'brand_LG', 'brand_Lenovo',
    'brand_MSI', 'brand_Microsoft', 'brand_Nokia',
    'brand_Realme', 'brand_Samsung', 'brand_Ultimus',
    'brand_Xiaomi',
    'os_Chrome', 'os_DOS', 'os_Mac',
    'os_Ubuntu', 'os_Windows'
]

input_data = pd.DataFrame(
    0,
    index=[0],
    columns=columns
)

# One Hot Encoding

input_data[f"brand_{brand}"] = 1
input_data[f"os_{os_name}"] = 1

# =====================================
# SSD
# =====================================

ssd = st.selectbox(
    "SSD (GB)",
    [0, 128, 256, 512, 1000, 2000]
)

input_data["ram(GB)"] = ram
input_data["ssd(GB)"] = ssd

# =====================================
# Hard Disk
# =====================================

hard_disk = st.selectbox(
    "Hard Disk (GB)",
    [0, 32, 64, 128, 1000]
)
input_data["Hard Disk(GB)"] = hard_disk
# =====================================
# screen_sizes
# =====================================
screen_sizes = [
    10.1, 11.6, 12.4, 13.0, 13.3, 13.4, 13.5,
    13.6, 14.0, 14.1, 14.2, 14.5,
    15.0, 15.56, 15.6, 16.0, 16.1,
    16.2, 17.0, 17.3, 17.32
]

screen_size = st.selectbox(
    "Screen Size (inches)",
    screen_sizes
)
input_data["screen_size(inches)"] = screen_size


# =====================================
# Graphics Card
# =====================================

gpu_type = st.selectbox(
    "Graphics Card",
    [
        "Integrated Graphics",
        "GTX / MX Series",
        "RTX 3050 / RX 6600M / RX 6650M",
        "RTX 3060",
        "RTX 3070 / RX 6800M / RX 6800S",
        "RTX 3080"
    ]
)

gpu_mapping = {
    "Integrated Graphics": 1,
    "GTX / MX Series": 2,
    "RTX 3050 / RX 6600M / RX 6650M": 3,
    "RTX 3060": 4,
    "RTX 3070 / RX 6800M / RX 6800S": 5,
    "RTX 3080": 5
}

gpu_score = gpu_mapping[gpu_type]
input_data["GPU_Score"] = gpu_score

# =====================================
# Graphics Memory (VRAM)
# =====================================

vram_options = {
    "Integrated Graphics (0 GB)": 0,
    "2 GB": 2,
    "4 GB": 4,
    "6 GB": 6,
    "8 GB": 8,
    "10 GB": 10,
    "12 GB": 12
}

selected_vram = st.selectbox(
    "Graphics Memory (VRAM)",
    list(vram_options.keys())
)

vram = vram_options[selected_vram]
input_data["VRAM_GB"] = vram

# =====================================
# CPU Brand
# =====================================

cpu_brand = st.selectbox(
    "CPU Brand",
    [
        "Intel",
        "AMD",
        "Apple"
    ]
)

# One-Hot Encoding

input_data["CPU_Brand_AMD"] = 0
input_data["CPU_Brand_Apple"] = 0
input_data["CPU_Brand_Intel"] = 0
input_data["CPU_Brand_Other"] = 0

if cpu_brand == "AMD":
    input_data["CPU_Brand_AMD"] = 1

elif cpu_brand == "Apple":
    input_data["CPU_Brand_Apple"] = 1

elif cpu_brand == "Intel":
    input_data["CPU_Brand_Intel"] = 1
# =====================================
#  CPU_Class
# =====================================
if cpu_brand == "Intel":

    processor_category = st.selectbox(
        "Processor Category",
        [
            "Core i3",
            "Core i5",
            "Core i7",
            "Core i9"
        ]
    )

    cpu_class_mapping = {
        "Core i3": 2,
        "Core i5": 3,
        "Core i7": 4,
        "Core i9": 5
    }

elif cpu_brand == "AMD":

    processor_category = st.selectbox(
        "Processor Category",
        [
            "Athlon",
            "Ryzen 3",
            "Ryzen 5",
            "Ryzen 7",
            "Ryzen 9"
        ]
    )

    cpu_class_mapping = {
        "Athlon": 1,
        "Ryzen 3": 2,
        "Ryzen 5": 3,
        "Ryzen 7": 4,
        "Ryzen 9": 5
    }

elif cpu_brand == "Apple":

    processor_category = st.selectbox(
        "Processor Category",
        [
            "M1",
            "M2",
            "M2 Max"
        ]
    )

    cpu_class_mapping = {
        "M1": 3,
        "M2": 4,
        "M2 Max": 5
    }

else:

    processor_category = st.selectbox(
        "Processor Category",
        [
            "Celeron",
            "Pentium",
            "Snapdragon",
            "Other"
        ]
    )

    cpu_class_mapping = {
        "Celeron": 1,
        "Pentium": 1,
        "Snapdragon": 1,
        "Other": 0
    }

cpu_class = cpu_class_mapping[processor_category]
input_data["CPU_Class"] = cpu_class

# =====================================
#  CPU_Generation
# =====================================

if cpu_brand == "Intel":

    generation_name = st.selectbox(
        "CPU Generation",
        [
            "10th Gen",
            "11th Gen",
            "12th Gen",
            "13th Gen"
        ]
    )

    generation_mapping = {
        "10th Gen": 10,
        "11th Gen": 11,
        "12th Gen": 12,
        "13th Gen": 13
    }

elif cpu_brand == "AMD":

    generation_name = st.selectbox(
        "CPU Generation",
        [
            "Ryzen 3000 Series",
            "Ryzen 4000 Series",
            "Ryzen 5000 Series",
            "Ryzen 6000 Series"
        ]
    )

    generation_mapping = {
        "Ryzen 3000 Series": 9,
        "Ryzen 4000 Series": 10,
        "Ryzen 5000 Series": 11,
        "Ryzen 6000 Series": 12
    }

elif cpu_brand == "Apple":

    generation_name = st.selectbox(
        "CPU Generation",
        [
            "Apple M1",
            "Apple M2"
        ]
    )

    generation_mapping = {
        "Apple M1": 11,
        "Apple M2": 12
    }

else:

    generation_name = st.selectbox(
        "CPU Generation",
        ["Other"]
    )

    generation_mapping = {
        "Other": 0
    }

cpu_generation = generation_mapping[generation_name]
input_data["CPU_Generation"] = cpu_generation

# =====================================
# num_of_cores
# =====================================

if cpu_class == 1:
    core_options = [2,4,8]

elif cpu_class == 2:
    core_options = [2,4,6,10]

elif cpu_class == 3:
    core_options = [4,6,8,10,12]

elif cpu_class == 4:
    core_options = [4,6,8,10,12,14,16]

elif cpu_class == 5:
    core_options = [8,12,14]
cores = st.selectbox(
    "Number of CPU Cores",
    core_options
)
input_data["no_of_cores"] = cores

# =====================================
# num_of_threads
# =====================================
if cpu_class == 1:
    thread_options = [2,4]

elif cpu_class == 2:
    thread_options = [4,8,12]

elif cpu_class == 3:
    thread_options = [6,8,12,16]

elif cpu_class == 4:
    thread_options = [8,12,16,20,24]

else:
    thread_options = [16,20]

threads = st.selectbox(
    "Number of CPU Threads",
    thread_options
)
input_data["no_of_threads"] = threads

st.write(input_data)

import joblib

# =====================================
# Load Model & Scaler
# =====================================

model = joblib.load("final_model.pkl")
scaler = joblib.load("scaler.pkl")

# =====================================
# Predict Button
# =====================================

feature_order = [
    'ram(GB)', 'ssd(GB)', 'Hard Disk(GB)',
    'screen_size(inches)', 'no_of_cores',
    'no_of_threads', 'GPU_Score', 'VRAM_GB',
    'CPU_Brand_AMD', 'CPU_Brand_Apple',
    'CPU_Brand_Intel', 'CPU_Brand_Other',
    'CPU_Generation', 'CPU_Class',
    'brand_AGB', 'brand_Acer', 'brand_Apple',
    'brand_Asus', 'brand_Avita', 'brand_Chuwi',
    'brand_Dell', 'brand_Fujitsu',
    'brand_Gigabyte', 'brand_HP',
    'brand_Honor', 'brand_Huawei',
    'brand_Infinix', 'brand_LG',
    'brand_Lenovo', 'brand_MSI',
    'brand_Microsoft', 'brand_Nokia',
    'brand_Realme', 'brand_Samsung',
    'brand_Ultimus', 'brand_Xiaomi',
    'os_Chrome', 'os_DOS',
    'os_Mac', 'os_Ubuntu',
    'os_Windows'
]

if st.button("Predict Price 💻"):

    input_data = input_data[feature_order]

    scaled_input = scaler.transform(input_data)

    prediction = model.predict(scaled_input)

    # =========================
    # Classification
    # =========================

    if (
        cpu_class >= 4 and
        gpu_score >= 4 and
        ram >= 16
    ):
        category = "High-End"

    elif (
        cpu_class >= 3 and
        ram >= 8
    ):
        category = "Mid-Range"

    else:
        category = "Low-End"

    # =========================
    # Results
    # =========================

    st.success(
        f"💰 Estimated Laptop Price: {prediction[0]:,.0f} EGP"
    )

    st.info(
        f"🏷️ Laptop Category: {category}"
    )