# Prebuilt-Kernel
rm -rf device/xiaomi/garnet-prebuilt
git clone https://github.com/los-garnet/android_device_xiaomi_garnet-kernel -b flare device/xiaomi/garnet-prebuilt --depth=1

# Vendor
rm -rf vendor/xiaomi/garnet
git clone https://github.com/los-garnet/proprietary_vendor_xiaomi_garnet -b flare vendor/xiaomi/garnet --depth=1

# MiuiCamera
rm -rf vendor/xiaomi/garnet-miuicamera
git clone https://codeberg.org/ramaadni/vendor_xiaomi_garnet-miuicamera vendor/xiaomi/garnet-miuicamera --depth=1

# Hw/ximi
rm -rf hardware/xiaomi
git clone https://github.com/los-garnet/android_hardware_xiaomi -b flare hardware/xiaomi
