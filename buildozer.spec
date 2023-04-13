[buildozer]
# (v1.0) Path to build artifact storage, absolute or relative to spec file
# build_dir = .buildozer

# (v1.0) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

# (v1.0) Path to build log storage, absolute or relative to spec file
# log_dir = .buildozer/logs

# (v1.0) verbosity (0 = no output, 1 = compile output, 2 = all output)
# verbosity = 1

# (v1.0) List of fnmatch patterns to exclude from the check for writable files
# exclude_patterns = []

# (v1.3) use_polly: if True, try to use manylinux2010 via polly when running in docker
# use_polly = False

# (v1.3) The name of the remote to use
# The default is origin
# remote = my-custom-name

# (v1.4) Directory containing any additional templates
# templates_dir = ~/.buildozer/templates/

# (v1.4) Directory containing any additional pre-build hooks
# pre_build_hooks_dir = hooks/pre-build/

# (v1.4) Directory containing any additional post-build hooks
# post_build_hooks_dir = hooks/post-build/

# (v1.4) Directory containing any additional source distribution hooks
# source_distribute_hooks_dir = hooks/source-distribute/

# (v1.4) Directory containing any additional android hooks
# android_hooks_dir = hooks/android/

# (v1.4) Directory containing any additional ios hooks
# ios_hooks_dir = hooks/ios/

# (v1.4) The number of threads to use for packaging
# package_threads = 1


# (app) Title of your application
[app]
# ime aplikacije
title = Song downloader

# ime paketa aplikacije (to ce se koristiti u android manifest-u)
package.name = song.downloader.app

# verzija aplikacije
version = 0.1  # or version.regex = '0\.1(\.\d+)?'

# putanja do glavnog python koda
source.dir = D:/Programing/PythonPrograming/Maturski

# moduli aplikacije, odvojeni zarezom
source.include_exts = py

# python for android url
requirements.python3 = kivy, pytube

# zavisnosti drugih biblioteka koje bi trebalo instalirati
requirements.host = python3, kivy, pytube

# zavisnosti biblioteka koje se koriste unutar android paketa
requirements = android

# verzija android sdk
android.sdk = 28

# verzija gradle-a
android.gradle_version = 4.4.1

# koji se način rada koristi za slanje logova za vrijeme izvršavanja aplikacije na daljinski server
logcat_filters = *:S python:D

# dodatne opcije koje ce se koristiti pri izgradnji
# može se definirati više opcija
#android.build.prop.myoption = myvalue

# putanja do python interpretatora (ukoliko nije uneseno, koristit ce se python3)
# unutar image/kivy je putanja gdje se nalazi python
#android
