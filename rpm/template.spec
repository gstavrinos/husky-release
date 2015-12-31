Name:           ros-indigo-husky-ur5-moveit-config
Version:        0.2.7
Release:        0%{?dist}
Summary:        ROS husky_ur5_moveit_config package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/husky_ur5_moveit_config
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-joint-state-publisher
Requires:       ros-indigo-moveit-planners-ompl
Requires:       ros-indigo-moveit-ros-benchmarks
Requires:       ros-indigo-moveit-ros-move-group
Requires:       ros-indigo-moveit-ros-visualization
Requires:       ros-indigo-moveit-ros-warehouse
Requires:       ros-indigo-moveit-setup-assistant
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-rviz
Requires:       ros-indigo-warehouse-ros
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslaunch

%description
An automatically generated package with all the configuration and launch files
for using the husky_ur5 with the MoveIt Motion Planning Framework

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Dec 31 2015 Devon Ash <dash@clearpathrobotics.com> - 0.2.7-0
- Autogenerated by Bloom

* Wed Jul 08 2015 Devon Ash <dash@clearpathrobotics.com> - 0.2.6-0
- Autogenerated by Bloom

* Thu Apr 16 2015 Devon Ash <dash@clearpathrobotics.com> - 0.2.5-0
- Autogenerated by Bloom

* Mon Apr 13 2015 Devon Ash <dash@clearpathrobotics.com> - 0.2.4-0
- Autogenerated by Bloom

* Wed Apr 08 2015 Devon Ash <dash@clearpathrobotics.com> - 0.2.3-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Devon Ash <dash@clearpathrobotics.com> - 0.2.2-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Devon Ash <dash@clearpathrobotics.com> - 0.2.1-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Devon Ash <dash@clearpathrobotics.com> - 0.2.0-0
- Autogenerated by Bloom

