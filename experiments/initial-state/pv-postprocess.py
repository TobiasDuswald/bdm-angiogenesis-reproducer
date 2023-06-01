# trace generated using paraview version 5.10.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

# Get the folder hosing the PVSM state via command line argument
import sys
folder = sys.argv[1]

# Verify that the folder exists and contains the PVSM state
import os
if not os.path.exists(folder):
    raise Exception("Folder " + folder + " does not exist")
if not os.path.exists(folder + "/angiogenesis.pvsm"):
    raise Exception("Folder " + folder + " does not contain the PVSM state")

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# determine if we are running on an apple system
is_apple = sys.platform == "darwin"

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# destroy renderView1
Delete(renderView1)
del renderView1

# load state
LoadState(folder + '/angiogenesis.pvsm')
LoadState(folder + '//angiogenesis.pvsm')

# find view
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')

# set active view
SetActiveView(renderView1)

# find source
vessels = FindSource('Vessels')
vessels.GlyphType.Resolution = 40

# set active source
SetActiveSource(vessels)

# get display properties
vesselsDisplay = GetDisplayProperties(vessels, view=renderView1)

# reset view to fit data
if is_apple:
    renderView1.ResetCamera(False)

# Properties modified on vesselsDisplay.DataAxesGrid
vesselsDisplay.DataAxesGrid.GridAxesVisibility = 1

# set scalar coloring
ColorBy(vesselsDisplay, ('POINTS', 'diameter_'))

# rescale color and/or opacity maps used to include current data range
vesselsDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
vesselsDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'diameter_'
diameter_LUT = GetColorTransferFunction('diameter_')
diameter_LUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
diameter_LUT.InterpretValuesAsCategories = 0
diameter_LUT.AnnotationsInitialized = 0
diameter_LUT.ShowCategoricalColorsinDataRangeOnly = 0
diameter_LUT.RescaleOnVisibilityChange = 0
diameter_LUT.EnableOpacityMapping = 0
diameter_LUT.RGBPoints = [13.352449829205808, 0.231373, 0.298039, 0.752941, 27.640411507258754, 0.865003, 0.865003, 0.865003, 41.928373185311706, 0.705882, 0.0156863, 0.14902]
diameter_LUT.UseLogScale = 0
diameter_LUT.UseOpacityControlPointsFreehandDrawing = 0
diameter_LUT.ShowDataHistogram = 0
diameter_LUT.AutomaticDataHistogramComputation = 0
diameter_LUT.DataHistogramNumberOfBins = 10
diameter_LUT.ColorSpace = 'Diverging'
diameter_LUT.UseBelowRangeColor = 0
diameter_LUT.BelowRangeColor = [0.0, 0.0, 0.0]
diameter_LUT.UseAboveRangeColor = 0
diameter_LUT.AboveRangeColor = [0.5, 0.5, 0.5]
diameter_LUT.NanColor = [1.0, 1.0, 0.0]
diameter_LUT.NanOpacity = 1.0
diameter_LUT.Discretize = 1
diameter_LUT.NumberOfTableValues = 256
diameter_LUT.ScalarRangeInitialized = 1.0
diameter_LUT.HSVWrap = 0
diameter_LUT.VectorComponent = 0
diameter_LUT.VectorMode = 'Magnitude'
diameter_LUT.AllowDuplicateScalars = 1
diameter_LUT.Annotations = []
diameter_LUT.ActiveAnnotatedValues = []
diameter_LUT.IndexedColors = []
diameter_LUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'diameter_'
diameter_PWF = GetOpacityTransferFunction('diameter_')
diameter_PWF.Points = [13.352449829205808, 0.0, 0.5, 0.0, 41.928373185311706, 1.0, 0.5, 0.0]
diameter_PWF.AllowDuplicateScalars = 1
diameter_PWF.UseLogScale = 0
diameter_PWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
diameter_LUT.ApplyPreset('erdc_red_BW', True)

# invert the transfer function
diameter_LUT.InvertTransferFunction()

# Rescale transfer function
diameter_LUT.RescaleTransferFunction(2.5, 42.0)

# Rescale transfer function
diameter_PWF.RescaleTransferFunction(2.5, 42.0)

# find source
tumorCells = FindSource('TumorCells')

# Fix resolution for spheres
tumorCells.GlyphType.ThetaResolution = 20
tumorCells.GlyphType.PhiResolution = 20

# set active source
SetActiveSource(tumorCells)

# get display properties
tumorCellsDisplay = GetDisplayProperties(tumorCells, view=renderView1)

# change solid color
tumorCellsDisplay.AmbientColor = [0.0, 0.6666666666666666, 0.0]
tumorCellsDisplay.DiffuseColor = [0.0, 0.6666666666666666, 0.0]

# set active source
SetActiveSource(vessels)

# reset view to fit data
if is_apple:
    renderView1.ResetCamera(True)

# Properties modified on renderView1
if is_apple:
    renderView1.UseColorPaletteForBackground = 0

# Properties modified on renderView1
renderView1.Background = [1.0, 1.0, 1.0]

# Properties modified on vesselsDisplay.DataAxesGrid
vesselsDisplay.DataAxesGrid.GridColor = [0.3382162203402762, 0.3382162203402762, 0.3382162203402762]

# Properties modified on vesselsDisplay.DataAxesGrid
vesselsDisplay.DataAxesGrid.XTitleColor = [0.49658960860608836, 0.49658960860608836, 0.49658960860608836]
vesselsDisplay.DataAxesGrid.YTitleColor = [0.49462119478141453, 0.49462119478141453, 0.49462119478141453]
vesselsDisplay.DataAxesGrid.ZTitleColor = [0.49837491416800184, 0.49837491416800184, 0.49837491416800184]
vesselsDisplay.DataAxesGrid.GridColor = [0.5028000305180438, 0.5028000305180438, 0.5028000305180438]
vesselsDisplay.DataAxesGrid.XLabelColor = [0.4981460288395514, 0.4981460288395514, 0.4981460288395514]
vesselsDisplay.DataAxesGrid.YLabelColor = [0.5042496375982299, 0.5042496375982299, 0.5042496375982299]
vesselsDisplay.DataAxesGrid.ZLabelColor = [0.4919050888838025, 0.4919050888838025, 0.4919050888838025]

# reset view to fit data
if is_apple:
    renderView1.ResetCamera(False)

# reset view to fit data
if is_apple:
    renderView1.ResetCamera(False)

# Properties modified on vesselsDisplay.DataAxesGrid
vesselsDisplay.DataAxesGrid.XTitleBold = 1
vesselsDisplay.DataAxesGrid.YTitleBold = 1
vesselsDisplay.DataAxesGrid.ZTitleBold = 1
vesselsDisplay.DataAxesGrid.XLabelBold = 1
vesselsDisplay.DataAxesGrid.YLabelBold = 1
vesselsDisplay.DataAxesGrid.ZLabelBold = 1

# Properties modified on vesselsDisplay.DataAxesGrid
vesselsDisplay.DataAxesGrid.ZAxisUseCustomLabels = 1
vesselsDisplay.DataAxesGrid.ZAxisLabels = [-1000.0, -750.0, -500.0, -250.0, 0.0, 250.0, 500.0, 750.0, 1000.0]

# Properties modified on vesselsDisplay.DataAxesGrid
vesselsDisplay.DataAxesGrid.ZLabelBold = 1

# Properties modified on vesselsDisplay.DataAxesGrid
vesselsDisplay.DataAxesGrid.XLabelFontSize = 24
vesselsDisplay.DataAxesGrid.YLabelFontSize = 24
vesselsDisplay.DataAxesGrid.ZLabelFontSize = 24

# Properties modified on vesselsDisplay.DataAxesGrid
vesselsDisplay.DataAxesGrid.XTitle = 'X Axis'
vesselsDisplay.DataAxesGrid.YTitle = 'Y Axis'
vesselsDisplay.DataAxesGrid.ZTitle = 'Z Axis'

# Properties modified on vesselsDisplay.DataAxesGrid
vesselsDisplay.DataAxesGrid.XTitleFontSize = 24
vesselsDisplay.DataAxesGrid.YTitleFontSize = 24
vesselsDisplay.DataAxesGrid.ZTitleFontSize = 24

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1282, 977)

# current camera placement for renderView1
renderView1.CameraPosition = [-5540.639525733534, -0.219818115234375, 2.53094482421875]
renderView1.CameraFocalPoint = [28.55023193359375, -0.219818115234375, 2.53094482421875]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 1441.412375074145

# Enable OSPRay for rendering on server
if not is_apple:
    pm = paraview.servermanager.vtkSMProxyManager
    if pm.GetVersionMajor() == 5 and pm.GetVersionMinor() < 7:
        renderView1.EnableOSPRay = 1
        renderView1.OSPRayRenderer = "pathtracer"
    else:
        renderView1.EnableRayTracing = 1
        renderView1.BackEnd = "OSPRay raycaster"
        renderView1.Denoise = 1
    # Properties modified on renderView1
    renderView1.Shadows = 1
    # Properties modified on renderView1
    renderView1.SamplesPerPixel = 10
    renderView1.AmbientSamples = 2
    # For unclear reasons, the line below makes our life miserable
    # renderView1.UseToneMapping = 1

# save screenshot
SaveScreenshot(folder + '/view1.png', renderView1, ImageResolution=[2564, 1954],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

# reset view to fit data
if is_apple:
    renderView1.ResetCamera(False)

# layout/tab size in pixels
layout1.SetSize(1282, 977)

# current camera placement for renderView1
renderView1.CameraPosition = [5597.739989600722, -0.219818115234375, 2.53094482421875]
renderView1.CameraFocalPoint = [28.55023193359375, -0.219818115234375, 2.53094482421875]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 1441.412375074145

# save screenshot
SaveScreenshot(folder + '/view2.png', renderView1, ImageResolution=[2564, 1954],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

# reset view to fit data
if is_apple:
    renderView1.ResetCamera(False)

# layout/tab size in pixels
layout1.SetSize(1282, 977)

# current camera placement for renderView1
renderView1.CameraPosition = [28.55023193359375, -5569.4095757823625, 2.53094482421875]
renderView1.CameraFocalPoint = [28.55023193359375, -0.219818115234375, 2.53094482421875]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 1441.412375074145

# save screenshot
SaveScreenshot(folder + '/view3.png', renderView1, ImageResolution=[2564, 1954],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

# reset view to fit data
if is_apple:
    renderView1.ResetCamera(False)

# layout/tab size in pixels
layout1.SetSize(1282, 977)

# current camera placement for renderView1
renderView1.CameraPosition = [28.55023193359375, 5568.969939551894, 2.53094482421875]
renderView1.CameraFocalPoint = [28.55023193359375, -0.219818115234375, 2.53094482421875]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 1441.412375074145

# save screenshot
SaveScreenshot(folder + '/view4.png', renderView1, ImageResolution=[2564, 1954],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

# reset view to fit data
if is_apple:
    renderView1.ResetCamera(False)

# layout/tab size in pixels
layout1.SetSize(1282, 977)

# current camera placement for renderView1
renderView1.CameraPosition = [28.55023193359375, -0.219818115234375, -5566.658812842909]
renderView1.CameraFocalPoint = [28.55023193359375, -0.219818115234375, 2.53094482421875]
renderView1.CameraParallelScale = 1441.412375074145

# save screenshot
SaveScreenshot(folder + '/view5.png', renderView1, ImageResolution=[2564, 1954],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

# reset view to fit data
if is_apple:
    renderView1.ResetCamera(False)

# layout/tab size in pixels
layout1.SetSize(1282, 977)

# current camera placement for renderView1
renderView1.CameraPosition = [28.55023193359375, -0.219818115234375, 5571.720702491347]
renderView1.CameraFocalPoint = [28.55023193359375, -0.219818115234375, 2.53094482421875]
renderView1.CameraParallelScale = 1441.412375074145

# save screenshot
SaveScreenshot(folder + '/view6.png', renderView1, ImageResolution=[2564, 1954],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1282, 977)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [28.55023193359375, -0.219818115234375, 5571.720702491347]
renderView1.CameraFocalPoint = [28.55023193359375, -0.219818115234375, 2.53094482421875]
renderView1.CameraParallelScale = 1441.412375074145

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
