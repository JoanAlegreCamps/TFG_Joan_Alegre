macro "Measure intensity over time [n3]" {
    // This macro measures the intensity of the selected ROI over all the frames in the stack
    nFrames = Stack.getDimensions()[4];
    for (i = 1; i <= nFrames; i++) {
        Stack.setFrame(i);
        run("Measure");
    }
}
