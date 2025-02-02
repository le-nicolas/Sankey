#this is only for demonstration purposes. you can tweak it however you want :)
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

def draw_sankey():
    fig, ax = plt.subplots(figsize=(8, 6))
    sankey = Sankey(ax=ax, unit=None)
    
    # Refrigerator energy flow
    sankey.add(
        flows=[3600, 6000, -8000, -2000],  # Energy values
        labels=["Work Input (3600 kJ)", "Cooling Effect (6000 kJ)", "Heat Rejected (8000 kJ)", "Net Energy Increase (2000 kJ)"],
        orientations=[0, 1, -1, 0],  # Direction of flow
        facecolor="lightblue"  # Single color for all flows
    )
    
    sankey.finish()
    ax.set_title("Energy Flow in Refrigerator-Kitchen System")
    plt.show()

# Run the function
draw_sankey()
