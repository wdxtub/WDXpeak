# Google Map V2 使用指南

最近在做地图相关的开发，但是网上对于 Google Map V2 的中文资料相当少，也比较凌乱，所以这里记录一下自己开发时候的经验，主要是自定义各类功能时候的记录。

## 写在前面

具体申请 google api key 和如何利用 MapFragment 来建立一个基本的地图视图这里不赘述，主要会集中在对地图本身的操作上。

## 添加/删除 Marker

添加 Marker 很简单，这里就用官方的例子来说明，在 `onMapReady` 方法中可以直接添加：

```java
@Override
public void onMapReady(GoogleMap googleMap) {
   mMap = googleMap;

   // Add a marker in Sydney and move the camera
   LatLng sydney = new LatLng(-34, 151);
   mMap.addMarker(new MarkerOptions().position(sydney).title("Marker in Sydney"));
   mMap.moveCamera(CameraUpdateFactory.newLatLng(sydney));
}
```

要删除 marker 有两种方式，一种是调用 maker 本身的 remove 方法，另一种是调用地图的 `clear()` 方法。

## 修改 Marker 的特性

其实就是修改以下对应的属性

```java
MarkerOptions markerOpt = new MarkerOptions();
markerOpt.position(new LatLng(fromLat, fromLng));
markerOpt.title("当前位置");
// 设定颜色：黄色
markerOpt.icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_YELLOW));
// 设为可以拖拽
markerOpt.draggable(true);
map.addMarker(markerOpt).showInfoWindow();


MarkerOptions markerOpt2 = new MarkerOptions();
markerOpt2.position(new LatLng(toLat, toLng));
markerOpt2.title("目标位置");
// 设定颜色：红色
markerOpt2.icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_RED));
map.addMarker(markerOpt2).showInfoWindow();
```

拖拽的话，默认长按进行拖动，只要注册事件监听就可以对拖拽进行操作：

```java
// mMap 是一个 Google Map instance
mMap.setOnMarkerDragListener(new GoogleMap.OnMarkerDragListener() {
  @Override
  public void onMarkerDragStart(Marker marker) {

  }

  @Override
  public void onMarkerDrag(Marker marker) {

  }

  @Override
  public void onMarkerDragEnd(Marker marker) {
      if(marker.isInfoWindowShown())
          marker.hideInfoWindow();
  }
});
```

Marker 更详细的用法可以看[这里](https://developers.google.com/maps/documentation/android-api/marker)

## Marker Cluster

当一个地方 marker 比较多之后，可以使用 Marker Cluster 聚合 marker。具体参考[这里](https://developers.google.com/maps/documentation/android-api/utility/marker-clustering)

## 在两点之间划线

传入两个位置即可

```java
PolylineOptions polylineOpt = new PolylineOptions();
polylineOpt.add(new LatLng(fromLat, fromLng));
polylineOpt.add(new LatLng(toLat, toLng));

// 颜色
polylineOpt.color(Color.BLUE);
// 宽度
polyline.setWidth(10);
Polyline polyline = map.addPolyline(polylineOpt);
```

## 设置 UI

基本上看下面的代码就可以明白：

```java
@Override
public void onMapReady(GoogleMap map) {
   mMap = map;

   mUiSettings = mMap.getUiSettings();

   // Keep the UI Settings state in sync with the checkboxes.
   // 控制缩放
   mUiSettings.setZoomControlsEnabled(isChecked(R.id.zoom_buttons_toggle));
   // 是否显示指南针
   mUiSettings.setCompassEnabled(isChecked(R.id.compass_toggle));
   // 是否指示我的位置按钮
   mUiSettings.setMyLocationButtonEnabled(isChecked(R.id.mylocationbutton_toggle));
   // 是否支持我的位置，需要和上面的配合使用
   mMap.setMyLocationEnabled(isChecked(R.id.mylocationlayer_toggle));
   // 是否支持滚动手势
   mUiSettings.setScrollGesturesEnabled(isChecked(R.id.scroll_toggle));
   // 是否支持缩放手势
   mUiSettings.setZoomGesturesEnabled(isChecked(R.id.zoom_gestures_toggle));
   // 是否支持倾斜手势
   mUiSettings.setTiltGesturesEnabled(isChecked(R.id.tilt_toggle));
   // 是否支持旋转手势
   mUiSettings.setRotateGesturesEnabled(isChecked(R.id.rotate_toggle));
}
```

其他一些功能

+ 层次缩放 `GoogleMap.getUiSettings().setIndoorLevelPickerEnabled(boolean)`
+ 地图工具（点击 marker 后会出现的小图标） `UiSettings.setMapToolbarEnabled(boolean).`

## 镜头转移动画

使用 `GoogleMap.moveCamera(CameraUpdate)` 的话镜头会瞬间移动，用户体验不好，可以使用 `GoogleMap.animateCamera(cameraUpdate, duration, callback)` 来慢慢移动地图

一个例子

```java
private static final LatLng SYDNEY = new LatLng(-33.88,151.21);
private static final LatLng MOUNTAIN_VIEW = new LatLng(37.4, -122.1);

private GoogleMap map;
... // Obtain the map from a MapFragment or MapView.

// Move the camera instantly to Sydney with a zoom of 15.
map.moveCamera(CameraUpdateFactory.newLatLngZoom(SYDNEY, 15));

// Zoom in, animating the camera.
map.animateCamera(CameraUpdateFactory.zoomIn());

// Zoom out to zoom level 10, animating with a duration of 2 seconds.
map.animateCamera(CameraUpdateFactory.zoomTo(10), 2000, null);

// Construct a CameraPosition focusing on Mountain View and animate the camera to that position.
CameraPosition cameraPosition = new CameraPosition.Builder()
    .target(MOUNTAIN_VIEW)      // Sets the center of the map to Mountain View
    .zoom(17)                   // Sets the zoom
    .bearing(90)                // Sets the orientation of the camera to east
    .tilt(30)                   // Sets the tilt of the camera to 30 degrees
    .build();                   // Creates a CameraPosition from the builder
map.animateCamera(CameraUpdateFactory.newCameraPosition(cameraPosition));
```

具体参考[这里](https://developers.google.com/maps/documentation/android-api/views)

## 参考资料

+ [Google Map API v2 （三）----- 地图上添加标记（Marker），标记info窗口，即指定经纬度获取地址字符串](http://www.cnblogs.com/inkheart0124/p/3536848.html)
+ [Android Google Maps V2之添加Pushpin(Marker)](http://blog.csdn.net/wannawang/article/details/17375111)


