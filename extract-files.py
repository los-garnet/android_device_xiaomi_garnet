#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
namespace_imports = [
    'device/xiaomi/garnet',
    'hardware/qcom-caf/sm8450',
    'hardware/qcom-caf/wlan',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qualcomm.qti.dpm.api@1.0',
        'vendor.qti.diaghal@1.0',
        'vendor.qti.hardware.dpmservice@1.0',
        'vendor.qti.hardware.dpmservice@1.1',
        'vendor.qti.hardware.qccsyshal@1.0',
        'vendor.qti.hardware.qccsyshal@1.1',
        'vendor.qti.hardware.qccvndhal@1.0',
        'vendor.qti.hardware.wifidisplaysession@1.0',
        'vendor.qti.imsrtpservice@3.0',
    ): lib_fixup_vendor_suffix,
    (
        'audio.primary.parrot',
        'libagm',
        'libagmclient',
        'libagmmixer',
        'libar-pal',
        'libpalclient',
	'libwpa_client',
        'vendor.qti.hardware.pal@1.0-impl',
        'libagm',
        'libagmclient',
        'libagmmixer',
        'libar-pal',
        'libpalclient',
	'libwpa_client',
        'vendor.qti.hardware.pal@1.0-impl',
        'vendor.qti.qccvndhal_aidl-v1-ndk',
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/lib64/libwfdmmsrc_system.so': blob_fixup()
        .add_needed('libgui_shim.so'),
    'system_ext/lib64/libwfdnative.so': blob_fixup()
        .add_needed('libbinder_shim.so')
        .add_needed('libinput_shim.so'),
    'system_ext/lib64/libwfdservice.so': blob_fixup()
        .replace_needed(
            'android.media.audio.common.types-V2-cpp.so',
            'android.media.audio.common.types-V4-cpp.so',
        )
        .replace_needed(
            'android.hardware.common-V2-ndk_platform.so',
            'android.hardware.common-V2-ndk.so',
        ),
    (
        'vendor/bin/hw/android.hardware.security.keymint-service-qti',
        'vendor/lib64/libqtikeymint.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.security.keymint-V1-ndk_platform.so',
            'android.hardware.security.keymint-V1-ndk.so',
        )
        .replace_needed(
            'android.hardware.security.secureclock-V1-ndk_platform.so',
            'android.hardware.security.secureclock-V1-ndk.so',
        )
        .replace_needed(
            'android.hardware.security.sharedsecret-V1-ndk_platform.so',
            'android.hardware.security.sharedsecret-V1-ndk.so',
        )
        .add_needed('android.hardware.security.rkp-V1-ndk.so'),
    'vendor/etc/camera/pureView_parameter.xml': blob_fixup()
        .regex_replace(r'=(\d+)>', r'="\1">'),
    (
        'vendor/etc/init/hw/init.batterysecret.rc',
        'vendor/etc/init/hw/init.mi_thermald.rc',
        'vendor/etc/init/hw/init.qti.kernel.rc',
    ): blob_fixup()
        .regex_replace(r'on charger', r'on property:init.svc.vendor.charger=running'),
    'vendor/etc/media_codecs_parrot_v0.xml': blob_fixup()
        .regex_replace(
            r'media_codecs_(google_audio|google_c2|google_telephony|vendor_audio)',
            ''
        ),
    'vendor/etc/seccomp_policy/c2audio.vendor.ext-arm64.policy': blob_fixup()
        .add_line_if_missing('setsockopt: 1\n'),
    'vendor/etc/vintf/manifest/c2_manifest_vendor.xml': blob_fixup()
        .regex_replace(r'.*\bdolby\b.*\n', ''),
    'vendor/lib64/vendor.libdpmframework.so': blob_fixup()
        .add_needed("libhidlbase_shim.so"),
    'vendor/etc/seccomp_policy/atfwd@2.0.policy': blob_fixup()
        .add_line_if_missing("gettid: 1"),
    'vendor/etc/seccomp_policy/wfdhdcphalservice.policy': blob_fixup()
        .add_line_if_missing("gettid: 1"),
    'vendor/bin/hw/vendor.dolby.hardware.dms@2.0-service': blob_fixup()
       .add_needed("libstagefright_foundation-v33.so"),
    'vendor/bin/qcc-trd': blob_fixup()
        .replace_needed(
            'libgrpc++_unsecure.so', 'libgrpc++_unsecure_prebuilt.so'
        ),
    'vendor/lib64/hw/audio.primary.parrot.so': blob_fixup()
        .replace_needed("libstagefright_foundation.so", "libstagefright_foundation-v33.so"),
    ('vendor/lib/libstagefright_soft_ac4dec.so', 'vendor/lib/libstagefright_soft_ddpdec.so', 'vendor/lib/libstagefrightdolby.so', 
     'vendor/lib64/libdlbdsservice.so', 'vendor/lib64/libstagefright_soft_ac4dec.so', 'vendor/lib64/libstagefright_soft_ddpdec.so', 
     'vendor/lib64/libstagefrightdolby.so'): blob_fixup()
        .replace_needed("libstagefright_foundation.so", "libstagefright_foundation-v33.so"),
}  # fmt: skip

module = ExtractUtilsModule(
    'garnet',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()