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

# find view
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')

# set active view
SetActiveView(renderView1)

# find source
tumorCells = FindSource('TumorCells')

# Fix resolution for spheres
tumorCells.GlyphType.ThetaResolution = 20
tumorCells.GlyphType.PhiResolution = 20

# set active source
SetActiveSource(tumorCells)

# get display properties
tumorCellsDisplay = GetDisplayProperties(tumorCells, view=renderView1)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(tumorCellsDisplay, ('POINTS', 'cell_state_'))

# rescale color and/or opacity maps used to include current data range
tumorCellsDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tumorCellsDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'cell_state_'
cell_state_LUT = GetColorTransferFunction('cell_state_')
cell_state_LUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
cell_state_LUT.InterpretValuesAsCategories = 0
cell_state_LUT.AnnotationsInitialized = 0
cell_state_LUT.ShowCategoricalColorsinDataRangeOnly = 0
cell_state_LUT.RescaleOnVisibilityChange = 0
cell_state_LUT.EnableOpacityMapping = 0
cell_state_LUT.RGBPoints = [3.0, 0.231373, 0.298039, 0.752941, 3.000244140625, 0.865003, 0.865003, 0.865003, 3.00048828125, 0.705882, 0.0156863, 0.14902]
cell_state_LUT.UseLogScale = 0
cell_state_LUT.UseOpacityControlPointsFreehandDrawing = 0
cell_state_LUT.ShowDataHistogram = 0
cell_state_LUT.AutomaticDataHistogramComputation = 0
cell_state_LUT.DataHistogramNumberOfBins = 10
cell_state_LUT.ColorSpace = 'Diverging'
cell_state_LUT.UseBelowRangeColor = 0
cell_state_LUT.BelowRangeColor = [0.0, 0.0, 0.0]
cell_state_LUT.UseAboveRangeColor = 0
cell_state_LUT.AboveRangeColor = [0.5, 0.5, 0.5]
cell_state_LUT.NanColor = [1.0, 1.0, 0.0]
cell_state_LUT.NanOpacity = 1.0
cell_state_LUT.Discretize = 1
cell_state_LUT.NumberOfTableValues = 256
cell_state_LUT.ScalarRangeInitialized = 1.0
cell_state_LUT.HSVWrap = 0
cell_state_LUT.VectorComponent = 0
cell_state_LUT.VectorMode = 'Magnitude'
cell_state_LUT.AllowDuplicateScalars = 1
cell_state_LUT.Annotations = []
cell_state_LUT.ActiveAnnotatedValues = []
cell_state_LUT.IndexedColors = []
cell_state_LUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'cell_state_'
cell_state_PWF = GetOpacityTransferFunction('cell_state_')
cell_state_PWF.Points = [3.0, 0.0, 0.5, 0.0, 3.00048828125, 1.0, 0.5, 0.0]
cell_state_PWF.AllowDuplicateScalars = 1
cell_state_PWF.UseLogScale = 0
cell_state_PWF.ScalarRangeInitialized = 1

# Properties modified on cell_state_LUT
cell_state_LUT.InterpretValuesAsCategories = 1
cell_state_LUT.AnnotationsInitialized = 1

# Properties modified on cell_state_LUT
cell_state_LUT.Annotations = ['3', '3']
cell_state_LUT.IndexedColors = [1.0, 1.0, 1.0]
cell_state_LUT.IndexedOpacities = [1.0]

# # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
# cell_state_LUT.ApplyPreset('CellColors', True)

# # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
# cell_state_LUT.ApplyPreset('CellColors', False)

# Properties modified on cell_state_LUT
cell_state_LUT.IndexedOpacities = [1.0, 1.0, 1.0, 1.0, 1.0]

# Properties modified on cell_state_LUT
cell_state_LUT.Annotations = ['0', 'Qz', '1', 'SG2', '2', 'G1', '3', 'Hypoxic', '4', 'Dead']

# Properties modified on cell_state_LUT
cell_state_LUT.Annotations = ['0', 'Q', '1', 'SG2', '2', 'G1', '3', 'Hypoxic', '4', 'Dead']

# Properties modified on cell_state_LUT
cell_state_LUT.IndexedColors = [1.0, 0.7372549019607844, 0.011764705882352941, 0.0, 0.3137254901960784, 0.0, 0.0, 1.0, 0.0, 0.32941176470588235, 0.32941176470588235, 0.32941176470588235, 0.07450980392156863, 0.07450980392156863, 0.07450980392156863]

# find source
vEGFconcentration = FindSource('VEGF-concentration')

# hide data in view
Hide(vEGFconcentration, renderView1)

# find source
nutrientsconcentration = FindSource('Nutrients-concentration')

# hide data in view
Hide(nutrientsconcentration, renderView1)

# find source
dOXconcentration = FindSource('DOX-concentration')

# hide data in view
Hide(dOXconcentration, renderView1)

# find source
tRAconcentration = FindSource('TRA-concentration')

# hide data in view
Hide(tRAconcentration, renderView1)

# find source
vessels = FindSource('Vessels')
vessels.GlyphType.Resolution = 40

# set active source
SetActiveSource(vessels)

# get display properties
vesselsDisplay = GetDisplayProperties(vessels, view=renderView1)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
if is_apple:
    renderView1.ResetCamera(False)

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

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.GoToLast()

# rescale color and/or opacity maps used to exactly fit the current data range
vesselsDisplay.RescaleTransferFunctionToDataRange(False, True)

# invert the transfer function
diameter_LUT.InvertTransferFunction()

animationScene1.GoToFirst()

# Properties modified on renderView1
if is_apple:
    renderView1.UseColorPaletteForBackground = 0

# Properties modified on renderView1
renderView1.Background = [1.0, 1.0, 1.0]

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# hide color bar/color legend
vesselsDisplay.SetScalarBarVisibility(renderView1, False)

# set active source
SetActiveSource(tumorCells)

# hide color bar/color legend
tumorCellsDisplay.SetScalarBarVisibility(renderView1, False)

# set active source
SetActiveSource(vEGFconcentration)

# get display properties
vEGFconcentrationDisplay = GetDisplayProperties(vEGFconcentration, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=vEGFconcentrationDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=vEGFconcentrationDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=vEGFconcentrationDisplay)

# show data in view
vEGFconcentrationDisplay = Show(vEGFconcentration, renderView1, 'UniformGridRepresentation')

# show color bar/color legend
vEGFconcentrationDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'SubstanceConcentration'
substanceConcentrationLUT = GetColorTransferFunction('SubstanceConcentration')
substanceConcentrationLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
substanceConcentrationLUT.InterpretValuesAsCategories = 0
substanceConcentrationLUT.AnnotationsInitialized = 0
substanceConcentrationLUT.ShowCategoricalColorsinDataRangeOnly = 0
substanceConcentrationLUT.RescaleOnVisibilityChange = 0
substanceConcentrationLUT.EnableOpacityMapping = 0
substanceConcentrationLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 5.878906683738906e-39, 0.865003, 0.865003, 0.865003, 1.1757813367477812e-38, 0.705882, 0.0156863, 0.14902]
substanceConcentrationLUT.UseLogScale = 0
substanceConcentrationLUT.UseOpacityControlPointsFreehandDrawing = 0
substanceConcentrationLUT.ShowDataHistogram = 0
substanceConcentrationLUT.AutomaticDataHistogramComputation = 0
substanceConcentrationLUT.DataHistogramNumberOfBins = 10
substanceConcentrationLUT.ColorSpace = 'Diverging'
substanceConcentrationLUT.UseBelowRangeColor = 0
substanceConcentrationLUT.BelowRangeColor = [0.0, 0.0, 0.0]
substanceConcentrationLUT.UseAboveRangeColor = 0
substanceConcentrationLUT.AboveRangeColor = [0.5, 0.5, 0.5]
substanceConcentrationLUT.NanColor = [1.0, 1.0, 0.0]
substanceConcentrationLUT.NanOpacity = 1.0
substanceConcentrationLUT.Discretize = 1
substanceConcentrationLUT.NumberOfTableValues = 256
substanceConcentrationLUT.ScalarRangeInitialized = 1.0
substanceConcentrationLUT.HSVWrap = 0
substanceConcentrationLUT.VectorComponent = 0
substanceConcentrationLUT.VectorMode = 'Magnitude'
substanceConcentrationLUT.AllowDuplicateScalars = 1
substanceConcentrationLUT.Annotations = []
substanceConcentrationLUT.ActiveAnnotatedValues = []
substanceConcentrationLUT.IndexedColors = []
substanceConcentrationLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'SubstanceConcentration'
substanceConcentrationPWF = GetOpacityTransferFunction('SubstanceConcentration')
substanceConcentrationPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
substanceConcentrationPWF.AllowDuplicateScalars = 1
substanceConcentrationPWF.UseLogScale = 0
substanceConcentrationPWF.ScalarRangeInitialized = 1

# Properties modified on vEGFconcentration
vEGFconcentration.TimeArray = 'None'

# update the view to ensure updated data information
renderView1.Update()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

# hide data in view
Hide(vEGFconcentration, renderView1)

# show data in view
vEGFconcentrationDisplay = Show(vEGFconcentration, renderView1, 'UniformGridRepresentation')

# show color bar/color legend
vEGFconcentrationDisplay.SetScalarBarVisibility(renderView1, True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
substanceConcentrationLUT.ApplyPreset('Linear Blue (8_31f)', True)

# rescale color and/or opacity maps used to exactly fit the current data range
vEGFconcentrationDisplay.RescaleTransferFunctionToDataRange(False, True)

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.11510670185089111, 0.06951871514320374, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.11510670185089111, 0.06417112052440643, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.10551447421312332, 0.010695187374949455, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.08313261717557907, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.07673779875040054, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.06714557111263275, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.2430030256509781, 0.14973261952400208, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.2430030256509781, 0.14438502490520477, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.2238185852766037, 0.06951871514320374, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.3229382336139679, 0.17112299799919128, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.3229382336139679, 0.16577540338039398, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.31014859676361084, 0.06951871514320374, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.27177971601486206, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.4124656617641449, 0.17112299799919128, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.4124656617641449, 0.11764705926179886, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.3740967810153961, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.36130714416503906, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.5051904916763306, 0.17112299799919128, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.5051904916763306, 0.14438502490520477, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4636242091655731, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04278074949979782, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.04812834411859512, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.053475938737392426, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.05882352963089943, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.06951871514320374, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.08021390438079834, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.08556149899959564, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.09090909361839294, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.11764705926179886, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.12834224104881287, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.12299465388059616, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.10695187747478485, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.09090909361839294, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.08021390438079834, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.6458764672279358, 0.32085561752319336, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.6458764672279358, 0.26737967133522034, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.6330868601799011, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5947179198265076, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.6874427795410156, 0.27807486057281494, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.6874427795410156, 0.27807486057281494, 0.5, 0.0, 0.7386013269424438, 0.3743315637111664, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.6874427795410156, 0.27807486057281494, 0.5, 0.0, 0.7386013269424438, 0.12299465388059616, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.6874427795410156, 0.27807486057281494, 0.5, 0.0, 0.6906402111053467, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.6874427795410156, 0.27807486057281494, 0.5, 0.0, 0.6874427795410156, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.6874427795410156, 0.27807486057281494, 0.5, 0.0, 0.6874427795410156, 0.0, 0.5, 0.0, 0.7929572463035583, 0.385026752948761, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.6874427795410156, 0.27807486057281494, 0.5, 0.0, 0.6874427795410156, 0.0, 0.5, 0.0, 0.7929572463035583, 0.385026752948761, 0.5, 0.0, 0.8377209901809692, 0.5080214142799377, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.6874427795410156, 0.27807486057281494, 0.5, 0.0, 0.6874427795410156, 0.0, 0.5, 0.0, 0.7929572463035583, 0.385026752948761, 0.5, 0.0, 0.8377209901809692, 0.22994652390480042, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.6874427795410156, 0.27807486057281494, 0.5, 0.0, 0.6874427795410156, 0.0, 0.5, 0.0, 0.7929572463035583, 0.385026752948761, 0.5, 0.0, 0.8281287550926208, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.6874427795410156, 0.27807486057281494, 0.5, 0.0, 0.6874427795410156, 0.0, 0.5, 0.0, 0.7929572463035583, 0.385026752948761, 0.5, 0.0, 0.8185365200042725, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.6874427795410156, 0.27807486057281494, 0.5, 0.0, 0.6874427795410156, 0.0, 0.5, 0.0, 0.7929572463035583, 0.385026752948761, 0.5, 0.0, 0.7929572463035583, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.6874427795410156, 0.27807486057281494, 0.5, 0.0, 0.6874427795410156, 0.0, 0.5, 0.0, 0.7929572463035583, 0.385026752948761, 0.5, 0.0, 0.7929572463035583, 0.0, 0.5, 0.0, 0.9144587516784668, 0.6096256971359253, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.6874427795410156, 0.27807486057281494, 0.5, 0.0, 0.6874427795410156, 0.0, 0.5, 0.0, 0.7929572463035583, 0.385026752948761, 0.5, 0.0, 0.7929572463035583, 0.0, 0.5, 0.0, 0.9144587516784668, 0.6096256971359253, 0.5, 0.0, 0.9400380253791809, 0.7379679083824158, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.6874427795410156, 0.27807486057281494, 0.5, 0.0, 0.6874427795410156, 0.0, 0.5, 0.0, 0.7929572463035583, 0.385026752948761, 0.5, 0.0, 0.7929572463035583, 0.0, 0.5, 0.0, 0.9144587516784668, 0.6096256971359253, 0.5, 0.0, 0.9400380253791809, 0.4491978585720062, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.05755335092544556, 0.07486630976200104, 0.5, 0.0, 0.05755335092544556, 0.0, 0.5, 0.0, 0.1438833773136139, 0.09090909361839294, 0.5, 0.0, 0.1438833773136139, 0.0, 0.5, 0.0, 0.23980562388896942, 0.11229946464300156, 0.5, 0.0, 0.23980562388896942, 0.0, 0.5, 0.0, 0.35491231083869934, 0.13368983566761017, 0.5, 0.0, 0.35491231083869934, 0.0, 0.5, 0.0, 0.4572293758392334, 0.15508021414279938, 0.5, 0.0, 0.4572293758392334, 0.0, 0.5, 0.0, 0.5563490390777588, 0.1818181872367859, 0.5, 0.0, 0.5563490390777588, 0.0, 0.5, 0.0, 0.6874427795410156, 0.27807486057281494, 0.5, 0.0, 0.6874427795410156, 0.0, 0.5, 0.0, 0.7929572463035583, 0.385026752948761, 0.5, 0.0, 0.7929572463035583, 0.0, 0.5, 0.0, 0.9144587516784668, 0.6096256971359253, 0.5, 0.0, 0.9144587516784668, 0.0, 0.5, 0.0, 0.9975914063814596, 1.0, 0.5, 0.0]

# Rescale transfer function
substanceConcentrationLUT.RescaleTransferFunction(1.0501237760755425e-149, 0.5)

# Rescale transfer function
substanceConcentrationPWF.RescaleTransferFunction(1.0501237760755425e-149, 0.5)

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.34455127376976963, 0.25668448209762573, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.385026752948761, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.6096256971359253, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.34455127376976963, 0.2139037549495697, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.385026752948761, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.6096256971359253, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.34455127376976963, 0.1764705926179886, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.385026752948761, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.6096256971359253, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.34455127376976963, 0.14973261952400208, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.385026752948761, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.6096256971359253, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.34455127376976963, 0.14438502490520477, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.385026752948761, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.6096256971359253, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.34455127376976963, 0.16042780876159668, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.385026752948761, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.6096256971359253, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.34455127376976963, 0.1978609710931778, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.385026752948761, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.6096256971359253, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3429487347602844, 0.2139037549495697, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.385026752948761, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.6096256971359253, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.385026752948761, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.6096256971359253, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.3743315637111664, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.6096256971359253, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.22994652390480042, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.6096256971359253, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.2192513346672058, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.6096256971359253, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.25668448209762573, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.6096256971359253, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.6096256971359253, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.45989304780960083, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.3582887649536133, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.32085561752319336, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4583333145357888, 0.30481284856796265, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.9625668525695801, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.6898396015167236, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.6096256971359253, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.5347593426704407, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.5026738047599792, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.4117647111415863, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.33689841628074646, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.24598930776119232, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.1978609710931778, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.2032085657119751, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.13903743028640747, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.13368983566761017, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.43108975887298584, 0.01604278013110161, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.13368983566761017, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.43108975887298584, 0.10160428285598755, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.13368983566761017, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.43108975887298584, 0.13903743028640747, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.13368983566761017, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.43108975887298584, 0.14973261952400208, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.13368983566761017, 0.5, 0.0]

# hide color bar/color legend
vEGFconcentrationDisplay.SetScalarBarVisibility(renderView1, False)

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.43589743971824646, 0.13903743028640747, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.13368983566761017, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4375, 0.10695187747478485, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.13368983566761017, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.442307710647583, 0.02139037474989891, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.13368983566761017, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.44391027092933655, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.13368983566761017, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4455128312110901, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.13368983566761017, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4455128312110901, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.12299465388059616, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4455128312110901, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.442307710647583, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4407051205635071, 0.0, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.4407051205635071, 0.01604278013110161, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.442307710647583, 0.026737969368696213, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.44391027092933655, 0.03208556026220322, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.44391027092933655, 0.03743315488100052, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4583333145357888, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.44391027092933655, 0.03743315488100052, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4615384638309479, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.44391027092933655, 0.03743315488100052, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4711538553237915, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.44391027092933655, 0.03743315488100052, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.47275641560554504, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.44391027092933655, 0.03743315488100052, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.48076924681663513, 0.005347593687474728, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.44391027092933655, 0.03743315488100052, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4791666865348816, 0.01604278013110161, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.44391027092933655, 0.03743315488100052, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4791666865348816, 0.02139037474989891, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.0501237760755425e-149, 0.0, 0.5, 0.0, 0.028846154125468815, 0.07486630976200104, 0.5, 0.0, 0.028846154125468815, 0.0, 0.5, 0.0, 0.07211538531367204, 0.09090909361839294, 0.5, 0.0, 0.07211538531367204, 0.0, 0.5, 0.0, 0.12019230636659695, 0.11229946464300156, 0.5, 0.0, 0.12019230636659695, 0.0, 0.5, 0.0, 0.17788460714896523, 0.13368983566761017, 0.5, 0.0, 0.17788460714896523, 0.0, 0.5, 0.0, 0.2291666572678944, 0.15508021414279938, 0.5, 0.0, 0.2291666572678944, 0.0, 0.5, 0.0, 0.2788461465881061, 0.1818181872367859, 0.5, 0.0, 0.2788461465881061, 0.0, 0.5, 0.0, 0.3413461446762085, 0.22994652390480042, 0.5, 0.0, 0.34455127376976963, 0.0, 0.5, 0.0, 0.39743588468741625, 0.26737967133522034, 0.5, 0.0, 0.39743588468741625, 0.0, 0.5, 0.0, 0.44391027092933655, 0.03743315488100052, 0.5, 0.0, 0.45673078298568726, 0.0, 0.5, 0.0, 0.4791666865348816, 0.026737969368696213, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0]

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(999, 840)

# current camera placement for renderView1
renderView1.CameraPosition = [-1187.8941474042674, 573.2625019925543, 586.7961761107416]
renderView1.CameraFocalPoint = [28.606781005859393, 0.5750122070312493, 2.5169677734374982]
renderView1.CameraViewUp = [0.41909654136195895, -0.035372467425866486, 0.907252378099198]
renderView1.CameraParallelScale = 1440.903955915933

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
SaveScreenshot(folder + '/ParaView/01-VEGF.png', renderView1, ImageResolution=[1998, 1680],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5',
    # MetaData=['Application', 'ParaView']
)

# hide data in view
Hide(vEGFconcentration, renderView1)

# Properties modified on animationScene1
animationScene1.AnimationTime = 100.0

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# hide data in view
Hide(tumorCells, renderView1)

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToPrevious()

animationScene1.GoToPrevious()

# set active source
SetActiveSource(tumorCells)

# show data in view
tumorCellsDisplay = Show(tumorCells, renderView1, 'GeometryRepresentation')

# hide color bar/color legend
tumorCellsDisplay.SetScalarBarVisibility(renderView1, False)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on animationScene1
animationScene1.AnimationTime = 80.0

# layout/tab size in pixels
layout1.SetSize(999, 840)

# current camera placement for renderView1
renderView1.CameraPosition = [-1187.8941474042674, 573.2625019925543, 586.7961761107416]
renderView1.CameraFocalPoint = [28.606781005859393, 0.5750122070312493, 2.5169677734374982]
renderView1.CameraViewUp = [0.41909654136195895, -0.035372467425866486, 0.907252378099198]
renderView1.CameraParallelScale = 1440.903955915933

# save screenshot
SaveScreenshot(folder + '/ParaView/02-proliferative-start.png', renderView1, ImageResolution=[1998, 1680],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5',
    # MetaData=['Application', 'ParaView']
)

# Properties modified on animationScene1
animationScene1.AnimationTime = 101.0

# layout/tab size in pixels
layout1.SetSize(999, 840)

# current camera placement for renderView1
renderView1.CameraPosition = [-1187.8941474042674, 573.2625019925543, 586.7961761107416]
renderView1.CameraFocalPoint = [28.606781005859393, 0.5750122070312493, 2.5169677734374982]
renderView1.CameraViewUp = [0.41909654136195895, -0.035372467425866486, 0.907252378099198]
renderView1.CameraParallelScale = 1440.903955915933

# save screenshot
SaveScreenshot(folder + '/ParaView/03-final-vasculature.png', renderView1, ImageResolution=[1998, 1680],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5',
    # MetaData=['Application', 'ParaView']
)

# set active source
SetActiveSource(tumorCells)

# set active source
SetActiveSource(nutrientsconcentration)

# get display properties
nutrientsconcentrationDisplay = GetDisplayProperties(nutrientsconcentration, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=nutrientsconcentrationDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=nutrientsconcentrationDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=nutrientsconcentrationDisplay)

# show data in view
nutrientsconcentrationDisplay = Show(nutrientsconcentration, renderView1, 'UniformGridRepresentation')

# hide color bar/color legend
nutrientsconcentrationDisplay.SetScalarBarVisibility(renderView1, False)

# Properties modified on nutrientsconcentration
nutrientsconcentration.TimeArray = 'None'

# update the view to ensure updated data information
renderView1.Update()

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
substanceConcentrationLUT.ApplyPreset('Linear Green (Gr4L)', True)

# rescale color and/or opacity maps used to exactly fit the current data range
nutrientsconcentrationDisplay.RescaleTransferFunctionToDataRange(False, True)

# invert the transfer function
substanceConcentrationLUT.InvertTransferFunction()

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.3217669153378796e-10, 0.0, 0.5, 0.0, 0.05701401319434254, 0.08556149899959564, 0.5, 0.0, 0.05701401319434254, 0.0, 0.5, 0.0, 0.1425350327875913, 0.09090909361839294, 0.5, 0.0, 0.1425350327875913, 0.0, 0.5, 0.0, 0.23755838297069404, 0.11229946464300156, 0.5, 0.0, 0.23755838297069404, 0.0, 0.5, 0.0, 0.35158639433350475, 0.13368983566761017, 0.5, 0.0, 0.35158639433350475, 0.0, 0.5, 0.0, 0.45294463649701716, 0.15508021414279938, 0.5, 0.0, 0.45294463649701716, 0.0, 0.5, 0.0, 0.5511354400510852, 0.1818181872367859, 0.5, 0.0, 0.5511354400510852, 0.0, 0.5, 0.0, 0.674665796710805, 0.22994652390480042, 0.5, 0.0, 0.6810006887456804, 0.0, 0.5, 0.0, 0.7855263695186372, 0.26737967133522034, 0.5, 0.0, 0.7855263695186372, 0.0, 0.5, 0.0, 0.8773823324566402, 0.03743315488100052, 0.5, 0.0, 0.9027218920618864, 0.0, 0.5, 0.0, 0.9470661360970336, 0.026737969368696213, 0.5, 0.0, 0.9882428836406423, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.3217669153378796e-10, 0.0, 0.5, 0.0, 0.05701401319434254, 0.0, 0.5, 0.0, 0.05701401319434254, 0.0, 0.5, 0.0, 0.1425350327875913, 0.09090909361839294, 0.5, 0.0, 0.1425350327875913, 0.0, 0.5, 0.0, 0.23755838297069404, 0.11229946464300156, 0.5, 0.0, 0.23755838297069404, 0.0, 0.5, 0.0, 0.35158639433350475, 0.13368983566761017, 0.5, 0.0, 0.35158639433350475, 0.0, 0.5, 0.0, 0.45294463649701716, 0.15508021414279938, 0.5, 0.0, 0.45294463649701716, 0.0, 0.5, 0.0, 0.5511354400510852, 0.1818181872367859, 0.5, 0.0, 0.5511354400510852, 0.0, 0.5, 0.0, 0.674665796710805, 0.22994652390480042, 0.5, 0.0, 0.6810006887456804, 0.0, 0.5, 0.0, 0.7855263695186372, 0.26737967133522034, 0.5, 0.0, 0.7855263695186372, 0.0, 0.5, 0.0, 0.8773823324566402, 0.03743315488100052, 0.5, 0.0, 0.9027218920618864, 0.0, 0.5, 0.0, 0.9470661360970336, 0.026737969368696213, 0.5, 0.0, 0.9882428836406423, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.3217669153378796e-10, 0.0, 0.5, 0.0, 0.05701401084661484, 0.0, 0.5, 0.0, 0.05701401319434254, 0.0, 0.5, 0.0, 0.1425350327875913, 0.09090909361839294, 0.5, 0.0, 0.1425350327875913, 0.0, 0.5, 0.0, 0.23755838297069404, 0.11229946464300156, 0.5, 0.0, 0.23755838297069404, 0.0, 0.5, 0.0, 0.35158639433350475, 0.13368983566761017, 0.5, 0.0, 0.35158639433350475, 0.0, 0.5, 0.0, 0.45294463649701716, 0.15508021414279938, 0.5, 0.0, 0.45294463649701716, 0.0, 0.5, 0.0, 0.5511354400510852, 0.1818181872367859, 0.5, 0.0, 0.5511354400510852, 0.0, 0.5, 0.0, 0.674665796710805, 0.22994652390480042, 0.5, 0.0, 0.6810006887456804, 0.0, 0.5, 0.0, 0.7855263695186372, 0.26737967133522034, 0.5, 0.0, 0.7855263695186372, 0.0, 0.5, 0.0, 0.8773823324566402, 0.03743315488100052, 0.5, 0.0, 0.9027218920618864, 0.0, 0.5, 0.0, 0.9470661360970336, 0.026737969368696213, 0.5, 0.0, 0.9882428836406423, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.3217669153378796e-10, 0.0, 0.5, 0.0, 0.05701401084661484, 0.0, 0.5, 0.0, 0.1425350327875913, 0.09090909361839294, 0.5, 0.0, 0.1425350327875913, 0.0, 0.5, 0.0, 0.23755838297069404, 0.11229946464300156, 0.5, 0.0, 0.23755838297069404, 0.0, 0.5, 0.0, 0.35158639433350475, 0.13368983566761017, 0.5, 0.0, 0.35158639433350475, 0.0, 0.5, 0.0, 0.45294463649701716, 0.15508021414279938, 0.5, 0.0, 0.45294463649701716, 0.0, 0.5, 0.0, 0.5511354400510852, 0.1818181872367859, 0.5, 0.0, 0.5511354400510852, 0.0, 0.5, 0.0, 0.674665796710805, 0.22994652390480042, 0.5, 0.0, 0.6810006887456804, 0.0, 0.5, 0.0, 0.7855263695186372, 0.26737967133522034, 0.5, 0.0, 0.7855263695186372, 0.0, 0.5, 0.0, 0.8773823324566402, 0.03743315488100052, 0.5, 0.0, 0.9027218920618864, 0.0, 0.5, 0.0, 0.9470661360970336, 0.026737969368696213, 0.5, 0.0, 0.9882428836406423, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.3217669153378796e-10, 0.0, 0.5, 0.0, 0.05701401084661484, 0.0, 0.5, 0.0, 0.1425350327875913, 0.0, 0.5, 0.0, 0.23755838297069404, 0.11229946464300156, 0.5, 0.0, 0.23755838297069404, 0.0, 0.5, 0.0, 0.35158639433350475, 0.13368983566761017, 0.5, 0.0, 0.35158639433350475, 0.0, 0.5, 0.0, 0.45294463649701716, 0.15508021414279938, 0.5, 0.0, 0.45294463649701716, 0.0, 0.5, 0.0, 0.5511354400510852, 0.1818181872367859, 0.5, 0.0, 0.5511354400510852, 0.0, 0.5, 0.0, 0.674665796710805, 0.22994652390480042, 0.5, 0.0, 0.6810006887456804, 0.0, 0.5, 0.0, 0.7855263695186372, 0.26737967133522034, 0.5, 0.0, 0.7855263695186372, 0.0, 0.5, 0.0, 0.8773823324566402, 0.03743315488100052, 0.5, 0.0, 0.9027218920618864, 0.0, 0.5, 0.0, 0.9470661360970336, 0.026737969368696213, 0.5, 0.0, 0.9882428836406423, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.3217669153378796e-10, 0.0, 0.5, 0.0, 0.05701401084661484, 0.0, 0.5, 0.0, 0.1425350327875913, 0.0, 0.5, 0.0, 0.23755838297069404, 0.0, 0.5, 0.0, 0.35158639433350475, 0.13368983566761017, 0.5, 0.0, 0.35158639433350475, 0.0, 0.5, 0.0, 0.45294463649701716, 0.15508021414279938, 0.5, 0.0, 0.45294463649701716, 0.0, 0.5, 0.0, 0.5511354400510852, 0.1818181872367859, 0.5, 0.0, 0.5511354400510852, 0.0, 0.5, 0.0, 0.674665796710805, 0.22994652390480042, 0.5, 0.0, 0.6810006887456804, 0.0, 0.5, 0.0, 0.7855263695186372, 0.26737967133522034, 0.5, 0.0, 0.7855263695186372, 0.0, 0.5, 0.0, 0.8773823324566402, 0.03743315488100052, 0.5, 0.0, 0.9027218920618864, 0.0, 0.5, 0.0, 0.9470661360970336, 0.026737969368696213, 0.5, 0.0, 0.9882428836406423, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.3217669153378796e-10, 0.0, 0.5, 0.0, 0.05701401084661484, 0.0, 0.5, 0.0, 0.1425350327875913, 0.0, 0.5, 0.0, 0.23755838297069404, 0.0, 0.5, 0.0, 0.35158639433350475, 0.0, 0.5, 0.0, 0.45294463649701716, 0.15508021414279938, 0.5, 0.0, 0.45294463649701716, 0.0, 0.5, 0.0, 0.5511354400510852, 0.1818181872367859, 0.5, 0.0, 0.5511354400510852, 0.0, 0.5, 0.0, 0.674665796710805, 0.22994652390480042, 0.5, 0.0, 0.6810006887456804, 0.0, 0.5, 0.0, 0.7855263695186372, 0.26737967133522034, 0.5, 0.0, 0.7855263695186372, 0.0, 0.5, 0.0, 0.8773823324566402, 0.03743315488100052, 0.5, 0.0, 0.9027218920618864, 0.0, 0.5, 0.0, 0.9470661360970336, 0.026737969368696213, 0.5, 0.0, 0.9882428836406423, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [1.3217669153378796e-10, 0.0, 0.5, 0.0, 0.05701401084661484, 0.0, 0.5, 0.0, 0.1425350327875913, 0.0, 0.5, 0.0, 0.23755838297069404, 0.0, 0.5, 0.0, 0.35158639433350475, 0.0, 0.5, 0.0, 0.45294463649701716, 0.0, 0.5, 0.0, 0.5511354400510852, 0.1818181872367859, 0.5, 0.0, 0.5511354400510852, 0.0, 0.5, 0.0, 0.674665796710805, 0.22994652390480042, 0.5, 0.0, 0.6810006887456804, 0.0, 0.5, 0.0, 0.7855263695186372, 0.26737967133522034, 0.5, 0.0, 0.7855263695186372, 0.0, 0.5, 0.0, 0.8773823324566402, 0.03743315488100052, 0.5, 0.0, 0.9027218920618864, 0.0, 0.5, 0.0, 0.9470661360970336, 0.026737969368696213, 0.5, 0.0, 0.9882428836406423, 0.0, 0.5, 0.0]

# Rescale transfer function
substanceConcentrationLUT.RescaleTransferFunction(0.5, 1.0)

# Rescale transfer function
substanceConcentrationPWF.RescaleTransferFunction(0.5, 1.0)

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5352563858032227, 0.010695187374949455, 0.5, 0.0, 0.572115385313672, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5352563858032227, 0.04812834411859512, 0.5, 0.0, 0.572115385313672, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5336538553237915, 0.10160428285598755, 0.5, 0.0, 0.572115385313672, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5336538553237915, 0.10695187747478485, 0.5, 0.0, 0.572115385313672, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5320512652397156, 0.10160428285598755, 0.5, 0.0, 0.572115385313672, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10160428285598755, 0.5, 0.0, 0.572115385313672, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.572115385313672, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5464743375778198, 0.03208556026220322, 0.5, 0.0, 0.572115385313672, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.572115385313672, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.05882352963089943, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5753205418586731, 0.05882352963089943, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5753205418586731, 0.06951871514320374, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5753205418586731, 0.09090909361839294, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5753205418586731, 0.10160428285598755, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5753205418586731, 0.09625668823719025, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5945512652397156, 0.03208556026220322, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5817307829856873, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5785256624221802, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6778846071489653, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.682692289352417, 0.01604278013110161, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.682692289352417, 0.13903743028640747, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.682692289352417, 0.12834224104881287, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.682692289352417, 0.11764705926179886, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.7067307829856873, 0.03208556026220322, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.620192306366597, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.005347593687474728, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.07486630976200104, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08021390438079834, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6458333134651184, 0.07486630976200104, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.629807710647583, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6282051205635071, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9439102709293365, 0.03743315488100052, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.942307710647583, 0.026737969368696213, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9391025900840759, 0.1871657818555832, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.942307710647583, 0.1925133764743805, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9455128312110901, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9551281929016113, 0.2085561603307724, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2139037549495697, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.026737969368696213, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9871795177459717, 0.03208556026220322, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9887820482254028, 0.10160428285598755, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9807692170143127, 0.02139037474989891, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9775640964508057, 0.005347593687474728, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.10695187747478485, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9903846383094788, 0.1818181872367859, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9903846383094788, 0.17112299799919128, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 1.0, 0.15508021414279938, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 1.0, 0.22994652390480042, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 1.0, 0.34224599599838257, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 1.0, 0.3957219421863556, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 1.0, 0.51871657371521, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 1.0, 0.5561497211456299, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 1.0, 0.5347593426704407, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 1.0, 0.732620358467102, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9695512652397156, 0.26737967133522034, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9903846383094788, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9887820482254028, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9743589758872986, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9663461446762085, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9743589758872986, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9759615659713745, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9775640964508057, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9791666865348816, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9807692170143127, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.1818181872367859, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.16042780876159668, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.11764705926179886, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.11229946464300156, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.08556149899959564, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.22994652390480042, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8413461446762085, 0.2085561603307724, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.08556149899959564, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.10160428285598755, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.10695187747478485, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26203209161758423, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.16577540338039398, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.17112299799919128, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.1925133764743805, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.2085561603307724, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.2032085657119751, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.2085561603307724, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.1978609710931778, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.2085561603307724, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.25668448209762573, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.2085561603307724, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.26737967133522034, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.2085561603307724, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.26203209161758423, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7379679083824158, 0.5, 0.0]

# layout/tab size in pixels
layout1.SetSize(999, 840)

# current camera placement for renderView1
renderView1.CameraPosition = [-1443.3593423703942, 693.5268748475143, 709.4948098615756]
renderView1.CameraFocalPoint = [28.606781005859393, 0.5750122070312493, 2.5169677734374982]
renderView1.CameraViewUp = [0.41909654136195895, -0.035372467425866486, 0.907252378099198]
renderView1.CameraParallelScale = 1440.903955915933

# save screenshot
SaveScreenshot(folder + '/ParaView/03-final-vasculature-with-nutrients.png', renderView1, ImageResolution=[1998, 1680],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5',
    # MetaData=['Application', 'ParaView']
)

# Properties modified on animationScene1
animationScene1.AnimationTime = 80.0

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.2085561603307724, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.26203209161758423, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.7486631274223328, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.2085561603307724, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.26203209161758423, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9197860956192017, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.2085561603307724, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.26203209161758423, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9251337051391602, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.2085561603307724, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.26203209161758423, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.2085561603307724, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.27807486057281494, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.2085561603307724, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.3582887649536133, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.34224599599838257, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.31550803780555725, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.26737967133522034, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.11764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.27272728085517883, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.10695187747478485, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.27272728085517883, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.14973261952400208, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.27272728085517883, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.1871657818555832, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.27272728085517883, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.778846146588106, 0.09625668823719025, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.1764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.27272728085517883, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.7788461446762085, 0.09090909361839294, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.1764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.27272728085517883, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.7788461446762085, 0.11229946464300156, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.1764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.27272728085517883, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.09625668823719025, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.7788461446762085, 0.12299465388059616, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.1764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.27272728085517883, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.12299465388059616, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.7788461446762085, 0.12299465388059616, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.1764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.27272728085517883, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.08556149899959564, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.12834224104881287, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.7788461446762085, 0.12299465388059616, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.1764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.27272728085517883, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.09090909361839294, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.12834224104881287, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.7788461446762085, 0.12299465388059616, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.1764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.27272728085517883, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5304487347602844, 0.10695187747478485, 0.5, 0.0, 0.5304487347602844, 0.0, 0.5, 0.0, 0.5769230723381042, 0.09625668823719025, 0.5, 0.0, 0.5769230723381042, 0.0, 0.5, 0.0, 0.6266025900840759, 0.11229946464300156, 0.5, 0.0, 0.6266025900840759, 0.0, 0.5, 0.0, 0.6875, 0.12834224104881287, 0.5, 0.0, 0.6875, 0.0, 0.5, 0.0, 0.7291666572678944, 0.0, 0.5, 0.0, 0.7788461446762085, 0.12299465388059616, 0.5, 0.0, 0.778846146588106, 0.0, 0.5, 0.0, 0.8445512737697696, 0.1764705926179886, 0.5, 0.0, 0.8445512737697696, 0.0, 0.5, 0.0, 0.8974358846874162, 0.27272728085517883, 0.5, 0.0, 0.8974358846874162, 0.0, 0.5, 0.0, 0.9567307829856873, 0.385026752948761, 0.5, 0.0, 0.9567307829856873, 0.0, 0.5, 0.0, 0.9823718070983887, 0.0, 0.5, 0.0, 1.0, 0.9304813146591187, 0.5, 0.0]

# layout/tab size in pixels
layout1.SetSize(999, 840)

# current camera placement for renderView1
renderView1.CameraPosition = [-1443.3593423703942, 693.5268748475143, 709.4948098615756]
renderView1.CameraFocalPoint = [28.606781005859393, 0.5750122070312493, 2.5169677734374982]
renderView1.CameraViewUp = [0.41909654136195895, -0.035372467425866486, 0.907252378099198]
renderView1.CameraParallelScale = 1440.903955915933

# save screenshot
SaveScreenshot(folder + '/ParaView/02-proliferative-start-with-nutrients.png', renderView1, ImageResolution=[1998, 1680],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5',
    # MetaData=['Application', 'ParaView']
)

# hide data in view
Hide(nutrientsconcentration, renderView1)

# Properties modified on animationScene1
animationScene1.AnimationTime = 150.0

# set active source
SetActiveSource(dOXconcentration)

# get display properties
dOXconcentrationDisplay = GetDisplayProperties(dOXconcentration, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=dOXconcentrationDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=dOXconcentrationDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=dOXconcentrationDisplay)

# show data in view
dOXconcentrationDisplay = Show(dOXconcentration, renderView1, 'UniformGridRepresentation')

# hide color bar/color legend
dOXconcentrationDisplay.SetScalarBarVisibility(renderView1, False)

# Properties modified on dOXconcentration
dOXconcentration.TimeArray = 'None'

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
substanceConcentrationLUT.RescaleTransferFunction(0.0, 1.0)

# Rescale transfer function
substanceConcentrationPWF.RescaleTransferFunction(0.0, 1.0)

# set active source
SetActiveSource(tRAconcentration)

# get display properties
tRAconcentrationDisplay = GetDisplayProperties(tRAconcentration, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=tRAconcentrationDisplay)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=tRAconcentrationDisplay.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=tRAconcentrationDisplay)

# show data in view
tRAconcentrationDisplay = Show(tRAconcentration, renderView1, 'UniformGridRepresentation')

# hide color bar/color legend
tRAconcentrationDisplay.SetScalarBarVisibility(renderView1, False)

# Properties modified on tRAconcentration
tRAconcentration.TimeArray = 'None'

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on animationScene1
animationScene1.AnimationTime = 149.0

# Properties modified on animationScene1
animationScene1.AnimationTime = 147.0

# hide data in view
Hide(dOXconcentration, renderView1)

# hide data in view
Hide(tRAconcentration, renderView1)

# layout/tab size in pixels
layout1.SetSize(999, 840)

# current camera placement for renderView1
renderView1.CameraPosition = [-1443.3593423703942, 693.5268748475143, 709.4948098615756]
renderView1.CameraFocalPoint = [28.606781005859393, 0.5750122070312493, 2.5169677734374982]
renderView1.CameraViewUp = [0.41909654136195895, -0.035372467425866486, 0.907252378099198]
renderView1.CameraParallelScale = 1440.903955915933

# save screenshot
SaveScreenshot(folder + '/ParaView/04-final-tumor-before-treatment.png', renderView1, ImageResolution=[1998, 1680],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5',
    # MetaData=['Application', 'ParaView']
)

# Properties modified on animationScene1
animationScene1.AnimationTime = 159.0

# Properties modified on animationScene1
animationScene1.AnimationTime = 155.0

# show data in view
tRAconcentrationDisplay = Show(tRAconcentration, renderView1, 'UniformGridRepresentation')

# hide color bar/color legend
tRAconcentrationDisplay.SetScalarBarVisibility(renderView1, False)

# rescale color and/or opacity maps used to exactly fit the current data range
tRAconcentrationDisplay.RescaleTransferFunctionToDataRange(False, True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
substanceConcentrationLUT.ApplyPreset('PuBu', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
substanceConcentrationLUT.ApplyPreset('PuBu', True)

# invert the transfer function
substanceConcentrationLUT.InvertTransferFunction()

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.02330629206952009, 0.10695187747478485, 0.5, 0.0, 0.02330629206952009, 0.0, 0.5, 0.0, 0.05887901763113958, 0.09625668823719025, 0.5, 0.0, 0.05887901763113958, 0.0, 0.5, 0.0, 0.09690507551419977, 0.11229946464300156, 0.5, 0.0, 0.09690507551419977, 0.0, 0.5, 0.0, 0.14351761403021912, 0.12834224104881287, 0.5, 0.0, 0.14351761403021912, 0.0, 0.5, 0.0, 0.17541040995396898, 0.0, 0.5, 0.0, 0.21343644461575859, 0.12299465388059616, 0.5, 0.0, 0.21343644607917708, 0.0, 0.5, 0.0, 0.26372894252005413, 0.1764705926179886, 0.5, 0.0, 0.26372894252005413, 0.0, 0.5, 0.0, 0.3042082661350788, 0.27272728085517883, 0.5, 0.0, 0.3042082661350788, 0.0, 0.5, 0.0, 0.34959419855071805, 0.385026752948761, 0.5, 0.0, 0.34959419855071805, 0.0, 0.5, 0.0, 0.3827136374139177, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.02330629206952009, 0.10695187747478485, 0.5, 0.0, 0.02330629206952009, 0.0, 0.5, 0.0, 0.05887901763113958, 0.09625668823719025, 0.5, 0.0, 0.05887901763113958, 0.0, 0.5, 0.0, 0.09690507551419977, 0.11229946464300156, 0.5, 0.0, 0.09690507551419977, 0.0, 0.5, 0.0, 0.14351761403021912, 0.12834224104881287, 0.5, 0.0, 0.14351761403021912, 0.0, 0.5, 0.0, 0.17541040995396898, 0.0, 0.5, 0.0, 0.21343644461575859, 0.12299465388059616, 0.5, 0.0, 0.21343644607917708, 0.0, 0.5, 0.0, 0.26372894252005413, 0.1764705926179886, 0.5, 0.0, 0.26372894252005413, 0.0, 0.5, 0.0, 0.3042082661350788, 0.27272728085517883, 0.5, 0.0, 0.3042082661350788, 0.0, 0.5, 0.0, 0.3495941758155823, 0.33689841628074646, 0.5, 0.0, 0.34959419855071805, 0.385026752948761, 0.5, 0.0, 0.34959419855071805, 0.0, 0.5, 0.0, 0.3827136374139177, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.02330629206952009, 0.10695187747478485, 0.5, 0.0, 0.02330629206952009, 0.0, 0.5, 0.0, 0.05887901763113958, 0.09625668823719025, 0.5, 0.0, 0.05887901763113958, 0.0, 0.5, 0.0, 0.09690507551419977, 0.11229946464300156, 0.5, 0.0, 0.09690507551419977, 0.0, 0.5, 0.0, 0.14351761403021912, 0.12834224104881287, 0.5, 0.0, 0.14351761403021912, 0.0, 0.5, 0.0, 0.17541040995396898, 0.0, 0.5, 0.0, 0.21343644461575859, 0.12299465388059616, 0.5, 0.0, 0.21343644607917708, 0.0, 0.5, 0.0, 0.26372894252005413, 0.1764705926179886, 0.5, 0.0, 0.26372894252005413, 0.0, 0.5, 0.0, 0.3042082661350788, 0.27272728085517883, 0.5, 0.0, 0.3042082661350788, 0.0, 0.5, 0.0, 0.34959419855071805, 0.385026752948761, 0.5, 0.0, 0.34959419855071805, 0.0, 0.5, 0.0, 0.3827136374139177, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.02330629206952009, 0.10695187747478485, 0.5, 0.0, 0.02330629206952009, 0.0, 0.5, 0.0, 0.05887901763113958, 0.09625668823719025, 0.5, 0.0, 0.05887901763113958, 0.0, 0.5, 0.0, 0.09690507551419977, 0.11229946464300156, 0.5, 0.0, 0.09690507551419977, 0.0, 0.5, 0.0, 0.14351761403021912, 0.12834224104881287, 0.5, 0.0, 0.14351761403021912, 0.0, 0.5, 0.0, 0.17541040995396898, 0.0, 0.5, 0.0, 0.21343644461575859, 0.12299465388059616, 0.5, 0.0, 0.21343644607917708, 0.0, 0.5, 0.0, 0.26372894252005413, 0.1764705926179886, 0.5, 0.0, 0.26372894252005413, 0.0, 0.5, 0.0, 0.3042082661350788, 0.27272728085517883, 0.5, 0.0, 0.3042082661350788, 0.0, 0.5, 0.0, 0.34959419855071805, 0.0, 0.5, 0.0, 0.3827136374139177, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.02330629206952009, 0.10695187747478485, 0.5, 0.0, 0.02330629206952009, 0.0, 0.5, 0.0, 0.05887901763113958, 0.09625668823719025, 0.5, 0.0, 0.05887901763113958, 0.0, 0.5, 0.0, 0.09690507551419977, 0.11229946464300156, 0.5, 0.0, 0.09690507551419977, 0.0, 0.5, 0.0, 0.14351761403021912, 0.12834224104881287, 0.5, 0.0, 0.14351761403021912, 0.0, 0.5, 0.0, 0.17541040995396898, 0.0, 0.5, 0.0, 0.21343644461575859, 0.12299465388059616, 0.5, 0.0, 0.21343644607917708, 0.0, 0.5, 0.0, 0.26372894252005413, 0.1764705926179886, 0.5, 0.0, 0.26372894252005413, 0.0, 0.5, 0.0, 0.3042082661350788, 0.27272728085517883, 0.5, 0.0, 0.3042082661350788, 0.0, 0.5, 0.0, 0.3827136374139177, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.02330629206952009, 0.0, 0.5, 0.0, 0.05887901763113958, 0.09625668823719025, 0.5, 0.0, 0.05887901763113958, 0.0, 0.5, 0.0, 0.09690507551419977, 0.11229946464300156, 0.5, 0.0, 0.09690507551419977, 0.0, 0.5, 0.0, 0.14351761403021912, 0.12834224104881287, 0.5, 0.0, 0.14351761403021912, 0.0, 0.5, 0.0, 0.17541040995396898, 0.0, 0.5, 0.0, 0.21343644461575859, 0.12299465388059616, 0.5, 0.0, 0.21343644607917708, 0.0, 0.5, 0.0, 0.26372894252005413, 0.1764705926179886, 0.5, 0.0, 0.26372894252005413, 0.0, 0.5, 0.0, 0.3042082661350788, 0.27272728085517883, 0.5, 0.0, 0.3042082661350788, 0.0, 0.5, 0.0, 0.3827136374139177, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.02330629206952009, 0.0, 0.5, 0.0, 0.05887901763113958, 0.0, 0.5, 0.0, 0.09690507551419977, 0.11229946464300156, 0.5, 0.0, 0.09690507551419977, 0.0, 0.5, 0.0, 0.14351761403021912, 0.12834224104881287, 0.5, 0.0, 0.14351761403021912, 0.0, 0.5, 0.0, 0.17541040995396898, 0.0, 0.5, 0.0, 0.21343644461575859, 0.12299465388059616, 0.5, 0.0, 0.21343644607917708, 0.0, 0.5, 0.0, 0.26372894252005413, 0.1764705926179886, 0.5, 0.0, 0.26372894252005413, 0.0, 0.5, 0.0, 0.3042082661350788, 0.27272728085517883, 0.5, 0.0, 0.3042082661350788, 0.0, 0.5, 0.0, 0.3827136374139177, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.02330629206952009, 0.0, 0.5, 0.0, 0.05887901763113958, 0.0, 0.5, 0.0, 0.09690507551419977, 0.0, 0.5, 0.0, 0.14351761403021912, 0.12834224104881287, 0.5, 0.0, 0.14351761403021912, 0.0, 0.5, 0.0, 0.17541040995396898, 0.0, 0.5, 0.0, 0.21343644461575859, 0.12299465388059616, 0.5, 0.0, 0.21343644607917708, 0.0, 0.5, 0.0, 0.26372894252005413, 0.1764705926179886, 0.5, 0.0, 0.26372894252005413, 0.0, 0.5, 0.0, 0.3042082661350788, 0.27272728085517883, 0.5, 0.0, 0.3042082661350788, 0.0, 0.5, 0.0, 0.3827136374139177, 0.9304813146591187, 0.5, 0.0]

# Rescale transfer function
substanceConcentrationLUT.RescaleTransferFunction(0.1, 0.3827136374139177)

# Rescale transfer function
substanceConcentrationPWF.RescaleTransferFunction(0.1, 0.3827136374139177)

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.12834224104881287, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.25766721568051687, 0.12299465388059616, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.1764705926179886, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.26203209161758423, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.12834224104881287, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.25766721568051687, 0.12299465388059616, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.1764705926179886, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.4331550896167755, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.12834224104881287, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.25766721568051687, 0.12299465388059616, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.1764705926179886, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.12834224104881287, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.2567610740661621, 0.13368983566761017, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.1764705926179886, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.12834224104881287, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.2576672167615559, 0.5508021712303162, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.1764705926179886, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.12834224104881287, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.2576672167615559, 0.5454545617103577, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.1764705926179886, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.12834224104881287, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4385026693344116, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.1764705926179886, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.12834224104881287, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4331550896167755, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.1764705926179886, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.12834224104881287, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.1764705926179886, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.12834224104881287, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.29300642013549805, 0.1818181872367859, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.12834224104881287, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.29300642013549805, 0.3743315637111664, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.12834224104881287, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.45989304780960083, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.12834224104881287, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.13368983566761017, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.31016042828559875, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.31550803780555725, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22957707850039008, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.31550803780555725, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.22867095470428467, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.31550803780555725, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.29411765933036804, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.3475935757160187, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14349440316351875, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14440053701400757, 0.0, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14983734488487244, 0.24598930776119232, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14893120527267456, 0.24598930776119232, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14530667662620544, 0.2085561603307724, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14893120527267456, 0.11764705926179886, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.16977228224277496, 0.16042780876159668, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.16977228224277496, 0.17112299799919128, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.1679600030183792, 0.23529411852359772, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.1688661426305771, 0.32085561752319336, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.17158455749738458, 0.33689841628074646, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.17158455749738458, 0.3475935757160187, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.13715146481990814, 0.11229946464300156, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.1389637440443039, 0.09090909361839294, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.151649609208107, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.15074346959590912, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.14893120527267456, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11721654511746321, 0.0, 0.5, 0.0, 0.13805760443210602, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# invert the transfer function
substanceConcentrationLUT.InvertTransferFunction()

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.11993493884801865, 0.0, 0.5, 0.0, 0.13805760443210602, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.12265333533287048, 0.16042780876159668, 0.5, 0.0, 0.13805760443210602, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.12265333533287048, 0.17112299799919128, 0.5, 0.0, 0.13805760443210602, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.12446559965610504, 0.1818181872367859, 0.5, 0.0, 0.13805760443210602, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.13171467185020447, 0.1764705926179886, 0.5, 0.0, 0.13805760443210602, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.13805760443210602, 0.1764705926179886, 0.5, 0.0, 0.13805760443210602, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.13805760443210602, 0.1978609710931778, 0.5, 0.0, 0.13805760443210602, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.13805760443210602, 0.1925133764743805, 0.5, 0.0, 0.13805760443210602, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.13805760443210602, 0.12299465388059616, 0.5, 0.0, 0.13805760443210602, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.13805760443210602, 0.11229946464300156, 0.5, 0.0, 0.13805760443210602, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.13805760443210602, 0.08021390438079834, 0.5, 0.0, 0.13805760443210602, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.13805760443210602, 0.08556149899959564, 0.5, 0.0, 0.13805760443210602, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.1, 0.0, 0.5, 0.0, 0.13805760443210602, 0.09625668823719025, 0.5, 0.0, 0.13805760443210602, 0.0, 0.5, 0.0, 0.17158455749738458, 0.34224599599838257, 0.5, 0.0, 0.17158455749738458, 0.0, 0.5, 0.0, 0.20601761403021912, 0.34224599599838257, 0.5, 0.0, 0.20601761403021912, 0.0, 0.5, 0.0, 0.2576672167615559, 0.4064171314239502, 0.5, 0.0, 0.2576672167615559, 0.0, 0.5, 0.0, 0.2948186877661002, 0.5133689641952515, 0.5, 0.0, 0.2948186877661002, 0.0, 0.5, 0.0, 0.32472108919759557, 0.5133689641952515, 0.5, 0.0, 0.32472108919759557, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Rescale transfer function
substanceConcentrationLUT.RescaleTransferFunction(0.05, 0.3827136374139176)

# Rescale transfer function
substanceConcentrationPWF.RescaleTransferFunction(0.05, 0.3827136374139176)

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13317841291427612, 0.32620322704315186, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.34224599599838257, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.2245989292860031, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.34224599599838257, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.25668448209762573, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.34224599599838257, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.26203209161758423, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.34224599599838257, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.25668448209762573, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.34224599599838257, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.2085561603307724, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.34224599599838257, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.1871657818555832, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.34224599599838257, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.1925133764743805, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.34224599599838257, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.32620322704315186, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.34224599599838257, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.24598930776119232, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.34224599599838257, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.24598930776119232, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.15450620651245117, 0.3957219421863556, 0.5, 0.0, 0.17476761403021912, 0.34224599599838257, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.24598930776119232, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.34224599599838257, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.23529411852359772, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.34224599599838257, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.16577540338039398, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.34224599599838257, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.17112299799919128, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.34224599599838257, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.17112299799919128, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.32085561752319336, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.17112299799919128, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.26737967133522034, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.17112299799919128, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.26203209161758423, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.17112299799919128, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.25668448209762573, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.17112299799919128, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.2513369023799896, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# Properties modified on substanceConcentrationPWF
substanceConcentrationPWF.Points = [0.05, 0.0, 0.5, 0.0, 0.09478837355598566, 0.09625668823719025, 0.5, 0.0, 0.09478837355598566, 0.0, 0.5, 0.0, 0.13424481650579217, 0.17112299799919128, 0.5, 0.0, 0.13424481650579217, 0.0, 0.5, 0.0, 0.17476761403021912, 0.25668448209762573, 0.5, 0.0, 0.17476761403021912, 0.0, 0.5, 0.0, 0.2355518314203665, 0.4064171314239502, 0.5, 0.0, 0.2355518314203665, 0.0, 0.5, 0.0, 0.27927381514307714, 0.5133689641952515, 0.5, 0.0, 0.27927381514307714, 0.0, 0.5, 0.0, 0.3144646776663372, 0.5133689641952515, 0.5, 0.0, 0.3144646776663372, 0.0, 0.5, 0.0, 0.3827136374139176, 0.9304813146591187, 0.5, 0.0]

# layout/tab size in pixels
layout1.SetSize(999, 840)

# current camera placement for renderView1
renderView1.CameraPosition = [-1443.3593423703942, 693.5268748475143, 709.4948098615756]
renderView1.CameraFocalPoint = [28.606781005859393, 0.5750122070312493, 2.5169677734374982]
renderView1.CameraViewUp = [0.41909654136195895, -0.035372467425866486, 0.907252378099198]
renderView1.CameraParallelScale = 1440.903955915933

# save screenshot
SaveScreenshot(folder + '/ParaView/05-treatment.png', renderView1, ImageResolution=[1998, 1680],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5',
    # MetaData=['Application', 'ParaView']
)

# hide data in view
Hide(tRAconcentration, renderView1)

# Properties modified on animationScene1
animationScene1.AnimationTime = 166.0

# Properties modified on animationScene1
animationScene1.AnimationTime = 178.0

# layout/tab size in pixels
layout1.SetSize(999, 840)

# current camera placement for renderView1
renderView1.CameraPosition = [-1443.3593423703942, 693.5268748475143, 709.4948098615756]
renderView1.CameraFocalPoint = [28.606781005859393, 0.5750122070312493, 2.5169677734374982]
renderView1.CameraViewUp = [0.41909654136195895, -0.035372467425866486, 0.907252378099198]
renderView1.CameraParallelScale = 1440.903955915933

# save screenshot
SaveScreenshot(folder + '/ParaView/06-post-treatment.png', renderView1, ImageResolution=[1998, 1680],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5',
    # MetaData=['Application', 'ParaView']
)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(999, 840)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-1443.3593423703942, 693.5268748475143, 709.4948098615756]
renderView1.CameraFocalPoint = [28.606781005859393, 0.5750122070312493, 2.5169677734374982]
renderView1.CameraViewUp = [0.41909654136195895, -0.035372467425866486, 0.907252378099198]
renderView1.CameraParallelScale = 1440.903955915933

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
