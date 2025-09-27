import geopandas as gpd
import matplotlib.pyplot as plt
# Load the OSINT data into a Geopandas DataFrame
data = gpd.read_file('../Data/geodata.csv')
# Plot the data on a map
data.plot()
# Add labels and title
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.title('OSINT Data Map')
# Display the map
plt.show()
