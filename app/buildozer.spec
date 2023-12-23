[app]

# (str) Title of your application
title = YourAppTitle

# (str) Package name
package.name = your_app_name

# (str) Package domain (needed for android/ios packaging)
package.domain = org.yourapp

source.dir = .
version = 1.0.0
version.filename = %(source.dir)s/lec2.py

# (str) Source code where the main.py lives
source.include_exts = py, png, jpg, kv, atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/ks.jpg

# (str) Icon of the application
icon.filename = %(source.dir)s/data/ks.jpg

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (list) Service to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 20

# (str) Android NDK version to use
android.ndk = 23b

# (int) Android NDK API to use.
android.ndk_api = 21

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (bool) Enable AndroidX support.
android.enable_androidx = True

# (list) Android AAR archives to add
# android.add_aars =

# (list) Android additional libraries to copy into libs/armeabi
# android.add_libs_armeabi =

# (bool) Indicate whether the screen should stay on
android.wakelock = False

# (str) Android application meta-data to set (key=value format)
# android.meta_data =

# (list) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# android.arch = armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (bool) Skip byte compile for .py files
# android.no-byte-compile-python = False

# (str) The format used to package the app for release mode (aab or apk or aar).
# android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar).
# android.debug_artifact = apk

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" as [section:key].
#    Each line will be considered as an option to the list.

#    -----------------------------------------------------------------------------
#    Profiles
#
#    You can extend sections / keys with a profile.
