#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
TARGET_SUPPORTS_OMX_SERVICE := false
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Fortune stuff.
$(call inherit-product, vendor/fortune/config/common_full_phone.mk)

# Inherit from garnet device
$(call inherit-product, device/xiaomi/garnet/device.mk)

# Fortune Stuff
TARGET_BOOT_ANIMATION_RES := 1080

PRODUCT_NAME := fortune_garnet
PRODUCT_DEVICE := garnet
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_BRAND := Redmi
PRODUCT_MODEL := 2312DRA50G

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="garnet_global-user 14 UKQ1.231003.002 V816.0.17.0.UNRMIXM release-keys" \
    BuildFingerprint=Redmi/garnet_global/garnet:14/UKQ1.231003.002/V816.0.17.0.UNRMIXM:user/release-keys \
    DeviceName=garnet \
    DeviceProduct=garnet_global

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi
