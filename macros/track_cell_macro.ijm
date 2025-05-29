macro "Track cell and measure G&R [n0]" {
    // Add the current ROI to the ROI Manager
    roiManager("Add");

    // Measure channel 2 (Green - mtDNA)
    Stack.setChannel(2);
    run("Measure");

    // Measure channel 3 (Red - mitochondria)
    Stack.setChannel(3);
    run("Measure");

    // Return to channel 1 (Brightfield)
    Stack.setChannel(1);
}
