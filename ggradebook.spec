Summary:	Ggradebook is the fully-featured GNU gradebook
Summary(hu.UTF-8):	Ggradebook egy lehetőségekben gazdag GNU osztálynapló
Name:		ggradebook
Version:	0.91
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnu.org/gnu/ggradebook/%{name}-%{version}.tar.gz
# Source0-md5:	bd973100fd811ed0a16cf677719988bc
URL:		http://www.gnu.org/software/ggradebook/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ggradebook is the fully-featured GNU gradebook; an application for
tracking student grades for teachers.

%description -l hu.UTF-8
Ggradebook egy lehetőségekben gazdag osztálynapló; egy alkalmazás,
amellyel a tanárok nyilvántarthatják a diákok eredményeit.

%prep
%setup -q -n Ggradebook-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
# we skip %{_datadir}/Ggradebook/help dir and its content, because the README is same in the %doc section
%dir %{_datadir}/Ggradebook
%dir %{_datadir}/Ggradebook/pix
%{_datadir}/Ggradebook/pix/*
