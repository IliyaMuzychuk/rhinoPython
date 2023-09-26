import rhinoscriptsyntax as rs
import scriptcontext as sc


def resetLayerStructure():
    # Get all layers in the Rhino document
    layers = rs.LayerNames()
    data = {}

    for layer in layers:
        
        print(layer)
        layer_id = rs.LayerId(layer)

        layer_name = rs.LayerName(layer_id)
        layer_color = rs.LayerColor(layer_id)
        layer_linetype = rs.LayerLinetype(layer_id)
        layer_print_color = rs.LayerPrintColor(layer)
        layer_print_width = rs.LayerPrintWidth(layer)


        data[layer_name] = {

            'layer color' : layer_color,
            'layer linetype' : layer_linetype,
            'layer print color' : layer_print_color,
            'layer print width' : layer_print_width,
        }
    
    return data

def ImportLayersFromFileTest():

    filename = 'Z:/BIM Standards/00_Rhino/Rhino Template/XXXXX.X_MODEL TEMPLATE.3dm'

    #filename=rs.OpenFileName("Choose file to import layers")

    if not filename: return

    read_file=Rhino.FileIO.File3dm.Read(filename)

    if read_file:

        layer_list=read_file.AllLayers
        print(layer_list)
        for layer in layer_list:
            sc.doc.Layers.Add(layer)

 

if __name__ == "__main__":
    ImportLayersFromFileTest()      
