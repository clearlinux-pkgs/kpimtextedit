#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kpimtextedit
Version  : 20.12.1
Release  : 27
URL      : https://download.kde.org/stable/release-service/20.12.1/src/kpimtextedit-20.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.12.1/src/kpimtextedit-20.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.12.1/src/kpimtextedit-20.12.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kpimtextedit-data = %{version}-%{release}
Requires: kpimtextedit-lib = %{version}-%{release}
Requires: kpimtextedit-license = %{version}-%{release}
Requires: kpimtextedit-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcodecs-dev
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kio-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : sonnet-dev
BuildRequires : syntax-highlighting-dev

%description
No detailed description available

%package data
Summary: data components for the kpimtextedit package.
Group: Data

%description data
data components for the kpimtextedit package.


%package dev
Summary: dev components for the kpimtextedit package.
Group: Development
Requires: kpimtextedit-lib = %{version}-%{release}
Requires: kpimtextedit-data = %{version}-%{release}
Provides: kpimtextedit-devel = %{version}-%{release}
Requires: kpimtextedit = %{version}-%{release}

%description dev
dev components for the kpimtextedit package.


%package lib
Summary: lib components for the kpimtextedit package.
Group: Libraries
Requires: kpimtextedit-data = %{version}-%{release}
Requires: kpimtextedit-license = %{version}-%{release}

%description lib
lib components for the kpimtextedit package.


%package license
Summary: license components for the kpimtextedit package.
Group: Default

%description license
license components for the kpimtextedit package.


%package locales
Summary: locales components for the kpimtextedit package.
Group: Default

%description locales
locales components for the kpimtextedit package.


%prep
%setup -q -n kpimtextedit-20.12.1
cd %{_builddir}/kpimtextedit-20.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610040771
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1610040771
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kpimtextedit
cp %{_builddir}/kpimtextedit-20.12.1/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kpimtextedit/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/kpimtextedit-20.12.1/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kpimtextedit/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/kpimtextedit-20.12.1/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kpimtextedit/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/kpimtextedit-20.12.1/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kpimtextedit/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kpimtextedit-20.12.1/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kpimtextedit/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kpimtextedit-20.12.1/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kpimtextedit/6f1f675aa5f6a2bbaa573b8343044b166be28399
cp %{_builddir}/kpimtextedit-20.12.1/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kpimtextedit/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/kpimtextedit-20.12.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kpimtextedit/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kpimtextedit-20.12.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kpimtextedit/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kpimtextedit-20.12.1/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kpimtextedit/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kpimtextedit-20.12.1/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kpimtextedit/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd
%find_lang libkpimtextedit

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kpimtextedit.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/AbstractMarkupBuilder
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/AbstractTextToSpeechInterface
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/EditorUtil
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/EmoticonUnicodeTab
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/MarkupDirector
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/PlainTextEditFindBar
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/PlainTextEditor
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/PlainTextEditorWidget
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/PlainTextMarkupBuilder
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/PlainTextSyntaxSpellCheckingHighlighter
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/RichTextComposer
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/RichTextComposerActions
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/RichTextComposerControler
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/RichTextComposerEmailQuoteHighlighter
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/RichTextComposerImages
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/RichTextComposerWidget
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/RichTextEditFindBar
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/RichTextEditor
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/RichTextEditorWidget
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/RichTextExternalComposer
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/SelectSpecialCharDialog
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/SlideContainer
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/TextEditFindBarBase
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/TextEditorCompleter
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/TextGotoLineWidget
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/TextHTMLBuilder
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/TextToSpeech
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/TextToSpeechActions
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/TextToSpeechInterface
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/TextToSpeechWidget
/usr/include/KF5/KPIMTextEdit/KPIMTextEdit/TextUtils
/usr/include/KF5/KPIMTextEdit/kpimtextedit/abstractmarkupbuilder.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/abstracttexttospeechinterface.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/editorutil.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/emoticonunicodetab.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/kpimtextedit_export.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/markupdirector.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/plaintexteditfindbar.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/plaintexteditor.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/plaintexteditorwidget.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/plaintextmarkupbuilder.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/plaintextsyntaxspellcheckinghighlighter.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/richtextcomposer.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/richtextcomposeractions.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/richtextcomposercontroler.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/richtextcomposeremailquotehighlighter.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/richtextcomposerimages.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/richtextcomposerwidget.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/richtexteditfindbar.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/richtexteditor.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/richtexteditorwidget.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/richtextexternalcomposer.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/selectspecialchardialog.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/slidecontainer.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/texteditfindbarbase.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/texteditorcompleter.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/textgotolinewidget.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/texthtmlbuilder.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/texttospeech.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/texttospeechactions.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/texttospeechinterface.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/texttospeechwidget.h
/usr/include/KF5/KPIMTextEdit/kpimtextedit/textutils.h
/usr/include/KF5/kpimtextedit_version.h
/usr/lib64/cmake/KF5PimTextEdit/KF5PimTextEditConfig.cmake
/usr/lib64/cmake/KF5PimTextEdit/KF5PimTextEditConfigVersion.cmake
/usr/lib64/cmake/KF5PimTextEdit/KF5PimTextEditTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5PimTextEdit/KF5PimTextEditTargets.cmake
/usr/lib64/libKF5PimTextEdit.so
/usr/lib64/qt5/mkspecs/modules/qt_KPIMTextEdit.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5PimTextEdit.so.5
/usr/lib64/libKF5PimTextEdit.so.5.16.1
/usr/lib64/qt5/plugins/designer/kpimtexteditwidgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kpimtextedit/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kpimtextedit/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kpimtextedit/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kpimtextedit/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kpimtextedit/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kpimtextedit/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kpimtextedit/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kpimtextedit/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libkpimtextedit.lang
%defattr(-,root,root,-)

