# Prebuilt-Kernel
echo "Clone Prebuilt kernel .."
rm -rf device/xiaomi/garnet-kernel
git clone https://github.com/los-garnet/android_device_xiaomi_garnet-kernel -b flare device/xiaomi/garnet-kernel --depth=1

# Vendor
echo "Clone Vendor .."
rm -rf vendor/xiaomi/garnet
git clone https://github.com/los-garnet/proprietary_vendor_xiaomi_garnet -b flare vendor/xiaomi/garnet --depth=1

# MiuiCamera
echo "Clone Miuicamera .."
rm -rf device/xiaomi/miuicamera-garnet && rm -rf vendor/xiaomi/miuicamera-garnet
git clone https://github.com/los-garnet/device_xiaomi_miuicamera-garnet device/xiaomi/miuicamera-garnet --depth=1
git clone https://codeberg.org/ramaadni/vendor_xiaomi_miuicamera-garnet.git vendor/xiaomi/miuicamera-garnet --depth=1

# Hw/ximi
echo "Clone Hardware Xiaomi .."
rm -rf hardware/xiaomi
git clone https://github.com/los-garnet/android_hardware_xiaomi -b flare hardware/xiaomi --depth=1
