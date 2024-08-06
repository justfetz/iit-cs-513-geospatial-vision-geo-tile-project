# Geospatial Vision Geo Tile Project

## About
This project is an attempt to utilize point clouds for geospatial vision. The goal is to process and visualize geospatial data using point cloud data. This project was developed as part of the CS-513 Geospatial Vision course at Illinois Institute of Technology. **Please note that this project is currently incomplete.**

## Features
- **Point Cloud Processing**: Initial steps towards processing point cloud data.
- **Geospatial Data Visualization**: Basic setup for visualizing geospatial data using point clouds.

## Example Code

### Sample Code
```python
import numpy as np
import open3d as o3d

# Load point cloud data
pcd = o3d.io.read_point_cloud("path/to/your/pointcloud.ply")

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd])

# Example point cloud processing (e.g., downsampling)
downsampled_pcd = pcd.voxel_down_sample(voxel_size=0.05)
o3d.visualization.draw_geometries([downsampled_pcd])
```

## Current Status
This project is currently incomplete. Several features and functionalities are yet to be implemented, including advanced point cloud processing and full geospatial data visualization.

## Future Work
Complete Point Cloud Processing: Implement advanced processing techniques for point clouds.
Enhance Visualization: Improve the visualization of geospatial data using point clouds.
Integrate Additional Data Sources: Combine point cloud data with other geospatial data sources for comprehensive analysis.
