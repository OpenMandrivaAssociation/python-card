%define name python-card
%define version 0.8.1

Name: %{name}
Summary: PythonCard GUI construction toolkit
Version: %{version}
Release: %mkrel 4
Source0: http://prdownloads.sourceforge.net/pythoncard/PythonCard-%{version}.tar.bz2
Patch1: PythonCardSamples.patch
Patch2: PythonCardConfig.patch
URL: http://pythoncard.sourceforge.net/
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
License: Python license
Requires: python-base >= %{pyver}, wxPython >= 2.5.2
BuildArch: noarch

%description
PythonCard is a GUI construction kit for building cross-platform desktop
applications on Windows, Mac OS X, and Linux, using the Python language.

%prep [ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%setup -n PythonCard-%{version} -q
%patch1 -p1
%patch2 -p1

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT
chmod 0755 %{buildroot}%py_puresitedir/PythonCard/flatfileDatabase.py
chmod 0755 %{buildroot}%py_puresitedir/PythonCard/gadflyDatabase.py
chmod 0755 %{buildroot}%py_puresitedir/PythonCard/templates/htmlpreview.py
chmod 0755 %{buildroot}%py_puresitedir/PythonCard/build/lib/PythonCard/flatfileDatabase.py
chmod 0755 %{buildroot}%py_puresitedir/PythonCard/build/lib/PythonCard/gadflyDatabase.py
chmod 0755 %{buildroot}%py_puresitedir/PythonCard/build/lib/PythonCard/templates/htmlpreview.py

install -m 0755 -d %{buildroot}%{_datadir}/PythonCard/samples
install -m 0755 -d %{buildroot}%{_datadir}/PythonCard/tools

cp -pr %{buildroot}%py_puresitedir/PythonCard/samples %{buildroot}%{_datadir}/PythonCard
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/samples.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/addresses/addresses.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/ataxx/ataxx.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/chat/chat.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/companies/companies.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/companies/parse_companies.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/conversions/conversions.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/custdb/custdb.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/dbBrowser/csvBrowse.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/dbBrowser/dbBrowser.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/dbBrowser/dbBrowser2.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/dbBrowser/dbLogin.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/dbBrowser/gadflyBrowse.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/dbBrowser/metakitBrowse.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/dbBrowser/mySQLBrowse.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/dbBrowser/oracleBrowse.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/dbBrowser/postgreBrowse.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/dbBrowser/pysqliteBrowse.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/dbBrowser/scripts/gadfly_sample.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/dbBrowser/scripts/mysql_sample.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/dialogs/dialogs.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/doodle/doodle.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/financial/mortgage.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/financial/pyfi.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/flatfileDatabase/flatfileDatabase.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/floatCanvasTest/floatCanvasTest.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/flock/flock.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/gadflyDatabase/gadflyDatabase.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/gravity/floatgravity.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/gravity/gravity.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/hopalong/hopalong.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/jabberChat/chatWindow.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/jabberChat/groupChatWindow.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/jabberChat/jabberChat.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/life/lexicon.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/life/life.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/life/patterns.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/lsystem/lsystem.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/lsystem/lsystemInteractive.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/minimal/minimal.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/minimalList/minimalList.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/minimalStandalone/minimal.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/minimalTree/minimalTree.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/moderator/moderator.py
chmod 0644 %{buildroot}%{_datadir}/PythonCard/samples/moderator/moderator.bat
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/montyhall/mh.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/montyhall/montyhall.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/mp3player/mp3player.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/multicolumnexample/multicolumnexample.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/noresource/noresource.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/pictureViewer/pictureViewer.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/proof/proof.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/pysshed/pysshed.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/radioclient/htmlpreview.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/radioclient/radioclient.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/redemo/redemo.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/reversi/reversi.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/rpn/rpn.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/saveClipboardBitmap/saveClipboardBitmap.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/searchexplorer/searchexplorer.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/simpleBrowser/simpleBrowser.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/simpleGrid/simpleGrid.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/simpleIEBrowser/simpleIEBrowser.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/slideshow/slideshow.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/sounds/sounds.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/SourceForgeTracker/SourceForgeTracker.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/spirograph/spirograph.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/spirographInteractive/spirographInteractive.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/stockprice/stockprice.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/testevents/testevents.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/testSplitter/doodle.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/testSplitter/minimal.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/testSplitter/testSplitter.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/textIndexer/textIndexer.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/textRouter/wordwrap.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/textRouter/textRouter.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/tictactoe/tictactoe.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/turtle/turtle.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/webgrabber/webchecker.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/webgrabber/webgrabber.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/webgrabber/websucker.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/webserver/console_server.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/webserver/oldModsWebserver.py
chmod 0644 %{buildroot}%{_datadir}/PythonCard/samples/webserver/runwebserver.bat
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/webserver/webserver.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/webserver/html/cgi-bin/contacts.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/webserver/html/cgi-bin/file_upload.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/webserver/html/cgi-bin/testenv.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/webserver/html/cgi-bin/webservices.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/widgets/widgets.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/samples/worldclock/worldclock.py

cp -pr %{buildroot}%py_puresitedir/PythonCard/tools %{buildroot}%{_datadir}/PythonCard
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/codeEditor/codeEditor.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/codeEditor/codeEditorR.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/codeEditor/restEditor.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/findfiles/findfiles.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/oneEditor/codePage.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/oneEditor/resourceEditor.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/oneEditor/restEditor.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/oneEditor/tabcodeEditor.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/oneEditor/modules/propertyEditor.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/oneEditor/templates/templateFullMenus.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/oneEditor/templates/templateNoMenus.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/oneEditor/templates/template.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/resourceEditor/resourceEditor.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/resourceEditor/templates/templateNoMenus.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/resourceEditor/modules/propertyEditor.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/resourceEditor/templates/templateFullMenus.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/resourceEditor/templates/template.py
chmod 0755 %{buildroot}%{_datadir}/PythonCard/tools/textEditor/textEditor.pyw

rm -rf %{buildroot}%py_puresitedir/PythonCard/samples
rm -rf %{buildroot}%py_puresitedir/PythonCard/tools
rm -rf %{buildroot}%py_puresitedir/PythonCard/docs
rm -f %{buildroot}/usr/bin/install-pythoncard.py
rm -f %{buildroot}%py_puresitedir/PythonCard/build/scripts-2.4/install-pythoncard.py

# menu support

# XDG menus
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-resourceEditor.desktop << EOXDG1
[Desktop Entry]
Name=PythonCard Resource Editor
Comment=This represents the beginnings of a GUI resource (layout) editor for PythonCard
Exec=%{_datadir}/PythonCard/tools/resourceEditor/resourceEditor.py
Icon=development_environment_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Development-DevelopmentEnvironments;Development;GUIDesigner;
EOXDG1

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-codeEditor.desktop << EOXDG2
[Desktop Entry]
Name=PythonCard Code Editor
Comment=The codeEditor sample in PythonCard is focused on being a simple to use Python source code editor
Exec=%{_datadir}/PythonCard/tools/codeEditor/codeEditor.py
Icon=editors_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Development-Tools;Development;
EOXDG2

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-samples.desktop << EOXDG3
[Desktop Entry]
Name=PythonCard Samples
Comment=The main purpose of the samples is to "stress" the PythonCard framework and make sure that the framework is robust and full-featured
Exec=%{_datadir}/PythonCard/samples/samples.py
Icon=toys_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Development-Tools;Development;
EOXDG3

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc docs/* README.txt README_StyleEditor.txt PKG-INFO
%py_puresitedir/PythonCard/*
%py_puresitedir/*.egg-info
%{_datadir}/PythonCard/samples/*
%{_datadir}/PythonCard/tools/*
%{_datadir}/applications/mandriva-%{name}*.desktop

%post
%{update_menus}

%postun
%{clean_menus}

