## An interactive map presentation as an alternative to static illustrations
By directly embedding the analysis results into an interactive map, it not only enhances interactivity during reading but also presents each data point in a more intuitive way compared to traditional static maps.I use ```pandas``` and ```folium``` to create interactive maps, so I first need to install ```pandas``` and ```folium``` in the working environment.

### Folium
Folium is a library used to create interactive maps in Python, built on top of the Leaflet.js library. It allows for easy visualization of geographic data and embedding it into Jupyter Notebooks or web applications. It supports many features such as marking points, heatmaps, layer controls, etc., and can output the results as HTML files, enabling users to interact with the map.

- Key features:

1. Interactive maps: Users can zoom, pan, click, and perform other actions, providing a rich interactive experience.
2. Geographic data visualization: It can display geographic coordinates, points, lines, areas, heatmaps, and visually represent them with geographic data such as latitude and longitude.
3. Custom styles: The appearance of the map can be adjusted, allowing customization of colors, icons, and more.
4. Supports multiple map layers: For example, OpenStreetMap, Stamen Terrain, CartoDB, etc.
5. Easy integration with Jupyter Notebooks: Suitable for data scientists' workflows, allowing maps to be displayed directly in Jupyter Notebooks.

In Folium, you can choose from various map types to visualize your data in different ways. Here are some of the popular map styles available:

- OpenStreetMap: The default map style in Folium, it provides detailed and open-source maps of the world.

```
folium.Map(location=[latitude, longitude], tiles='OpenStreetMap')
```

- Stamen Terrain: A topographical map with shaded relief, good for visualizing physical landscapes.
```
folium.Map(location=[latitude, longitude], tiles='Stamen Terrain')
```

- Stamen Toner: A black-and-white map style suitable for emphasizing other data layers, like points or heatmaps.
```
folium.Map(location=[latitude, longitude], tiles='Stamen Toner')
```

- Stamen Watercolor: A watercolor-like map style with artistic, soft colors, perfect for creative data visualizations.
```
folium.Map(location=[latitude, longitude], tiles='Stamen Watercolor')
```

- CartoDB positron: A light, minimalist map style from CartoDB, useful for emphasizing the data over the map itself.
```
folium.Map(location=[latitude, longitude], tiles='CartoDB positron')
```
