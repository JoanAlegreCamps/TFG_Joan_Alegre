macro "Measure all ROIs over time" {
    nFrames = Stack.getDimensions()[4]; // Get total number of frames
    nROIs = roiManager("count");

    for (r = 0; r < nROIs; r++) {
        roiManager("Select", r); // Select ROI r

        for (f = 1; f <= nFrames; f++) {
            Stack.setFrame(f);
            run("Measure");
        }
    }
}
