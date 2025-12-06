import onnxruntime as ot
import numpy as np
import pandas as pd 
Model = ot.InferenceSession("Possum age prediction model.onnx")
def Outliers_Treatment(df):
    L1 = 81.88283615714641 
    U1 = 103.32293307362283
    L2 = 53.4125  
    U2 = 62.7875
    L3 = 31.131060098837576 
    U3 =  42.888170670393194
    L4 = 11.895031140008312 
    U4 =  18.197276552299382
    L5 = 20.86320978240601 
    U5  =  33.13679021759399
    L6 = 24.300692309661358 
    U6 =  40.87238461341556
    L_ = 74.15681322875352 
    U_ =  100.02010984816957
    L7 = 55.27330588704665  
    U7 = 81.6451407148951
    L8 = 35.802628776911746  
    U8 = 60.45890968462672
    df['hdlngth'] = df['hdlngth'].clip(lower = L1 , upper = U1)
    df['skullw'] = df['skullw'].clip(lower = L2 , upper = U2)
    df['taill'] = df['taill'].clip(lower = L3 , upper = U3)
    df['eye'] = df['eye'].clip(lower = L4 , upper = U4)
    df['chest'] = df['chest'].clip(lower = L5 , upper = U5)
    df['belly'] = df['belly'].clip(lower = L6 , upper = U6)
    df['totlngth'] = df['totlngth'].clip(lower = L_ , upper = U_)
    df['footlgth'] = df['footlgth'].clip(lower = L7 , upper = U7)
    df['earconch'] = df['earconch'].clip(lower = L8 , upper = U8)  
    return df
def Predictor(input_param):
    input_df = pd.DataFrame(
    [input_param] , columns = ["hdlngth", "sex", "skullw", "totlngth", "taill",
    "footlgth", "earconch", "eye", "chest", "belly", "Pop"]
    )
    input_df = Outliers_Treatment(input_df)
    input_dict = {
        "hdlngth":np.array([[input_df['hdlngth'].iloc[0]]] , dtype = np.float32) , 
        "sex":np.array([[input_df['sex'].iloc[0]]] , dtype = object) , 
        "skullw":   np.array([[input_df["skullw"].iloc[0]]], dtype=np.float32),
        "totlngth": np.array([[input_df["totlngth"].iloc[0]]], dtype=np.float32),
        "taill":    np.array([[input_df["taill"].iloc[0]]], dtype=np.float32),
        "footlgth": np.array([[input_df["footlgth"].iloc[0]]], dtype=np.float32),
        "earconch": np.array([[input_df["earconch"].iloc[0]]], dtype=np.float32),
        "eye":      np.array([[input_df["eye"].iloc[0]]], dtype=np.float32),
        "chest":    np.array([[input_df["chest"].iloc[0]]], dtype=np.float32),
        "belly":    np.array([[input_df["belly"].iloc[0]]], dtype=np.float32),
        "Pop":      np.array([[input_df["Pop"].iloc[0]]], dtype=object),
    }
    prediction = Model.run(None , input_dict)
    return prediction[0][0][0]
