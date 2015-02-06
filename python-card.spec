Name: python-card
Summary: PythonCard GUI construction toolkit
Version: 0.8.2
Release: 2
Source0: https://sourceforge.net/projects/pythoncard/files/PythonCard/0.8.2/PythonCard-%{version}.tar.gz
Patch1: PythonCardSamples.patch
Patch2: PythonCardConfig.patch
URL: http://pythoncard.sourceforge.net/
Group: Development/Python
License: Python license
Requires: python-base >= %{py_ver}, wxPython >= 2.5.2
BuildArch: noarch
BuildRequires: python-devel 

%description
PythonCard is a GUI construction kit for building cross-platform desktop
applications on Windows, Mac OS X, and Linux, using the Python language.

%prep
%setup -n PythonCard-%{version} -q
%patch1 -p1
%patch2 -p1

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}
chmod 0755 %{buildroot}%{py_puresitedir}/PythonCard/gadflyDatabase.py
chmod 0755 %{buildroot}%{py_puresitedir}/PythonCard/templates/htmlpreview.py
chmod 0755 %{buildroot}%{py_puresitedir}/PythonCard/build/lib/PythonCard/flatfileDatabase.py
chmod 0755 %{buildroot}%{py_puresitedir}/PythonCard/build/lib/PythonCard/gadflyDatabase.py
chmod 0755 %{buildroot}%{py_puresitedir}/PythonCard/build/lib/PythonCard/templates/htmlpreview.py

install -m 0755 -d %{buildroot}%{_datadir}/PythonCard/samples
install -m 0755 -d %{buildroot}%{_datadir}/PythonCard/tools

cp -pr %{buildroot}%{py_puresitedir}/PythonCard/samples %{buildroot}%{_datadir}/PythonCard
cp -pr %{buildroot}%{py_puresitedir}/PythonCard/tools %{buildroot}%{_datadir}/PythonCard

# Mark all *py files in tools/ and samples/ that starts with shebang executable
find %{buildroot}%{_datadir}/PythonCard/samples/ \
     %{buildroot}%{_datadir}/PythonCard/tools/ \
     -name "*.py" | while read f
do
    file_start=`head -1 "$f"`
    if [[ $file_start == "#!/usr/bin/python" ]]
    then
	chmod 0755 $f
    fi
done

rm -rf %{buildroot}%{py_puresitedir}/PythonCard/samples
rm -rf %{buildroot}%{py_puresitedir}/PythonCard/tools
rm -rf %{buildroot}%{py_puresitedir}/PythonCard/docs
rm -f %{buildroot}/usr/bin/install-pythoncard.py
rm -f %{buildroot}%{py_puresitedir}/PythonCard/build/scripts-2.4/install-pythoncard.py

# menu support

# XDG menus
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}-resourceEditor.desktop << EOXDG1
[Desktop Entry]
Name=PythonCard Resource Editor
Comment=This represents the beginnings of a GUI resource (layout) editor for PythonCard
Exec=%{_datadir}/PythonCard/tools/resourceEditor/resourceEditor.py
Icon=development_environment_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Development-DevelopmentEnvironments;Development;GUIDesigner;
EOXDG1

cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}-codeEditor.desktop << EOXDG2
[Desktop Entry]
Name=PythonCard Code Editor
Comment=The codeEditor sample in PythonCard is focused on being a simple to use Python source code editor
Exec=%{_datadir}/PythonCard/tools/codeEditor/codeEditor.py
Icon=editors_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Development-Tools;Development;
EOXDG2

cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}-samples.desktop << EOXDG3
[Desktop Entry]
Name=PythonCard Samples
Comment=The main purpose of the samples is to "stress" the PythonCard framework and make sure that the framework is robust and full-featured
Exec=%{_datadir}/PythonCard/samples/samples.py
Icon=toys_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Development-Tools;Development;
EOXDG3

%files
%defattr(-,root,root,0755)
%doc docs/* README.txt README_StyleEditor.txt PKG-INFO
%{py_puresitedir}/PythonCard/*
%{py_puresitedir}/*.egg-info
%{_datadir}/PythonCard/samples/*
%{_datadir}/PythonCard/tools/*
%{_datadir}/applications/mandriva-%{name}*.desktop


