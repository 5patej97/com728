def cross_bridge(steps):
    for step in range(steps):
        print("Crossed step.")

    # Display message
    if steps > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")

cross_bridge(3)
cross_bridge(6)

cross_bridge(3)
cross_bridge(6)
