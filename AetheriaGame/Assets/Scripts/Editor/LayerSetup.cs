using UnityEngine;
using UnityEditor;

public class LayerSetup : EditorWindow
{
    [MenuItem("Tools/Setup Layers")]
    public static void SetupLayers()
    {
        // Crear la capa Ground si no existe
        SerializedObject tagManager = new SerializedObject(AssetDatabase.LoadAllAssetsAtPath("ProjectSettings/TagManager.asset")[0]);
        SerializedProperty layers = tagManager.FindProperty("layers");

        bool groundLayerExists = false;
        for (int i = 8; i < layers.arraySize; i++)
        {
            SerializedProperty layerSP = layers.GetArrayElementAtIndex(i);
            if (layerSP.stringValue == "Ground")
            {
                groundLayerExists = true;
                break;
            }
        }

        if (!groundLayerExists)
        {
            for (int i = 8; i < layers.arraySize; i++)
            {
                SerializedProperty layerSP = layers.GetArrayElementAtIndex(i);
                if (layerSP.stringValue == "")
                {
                    layerSP.stringValue = "Ground";
                    tagManager.ApplyModifiedProperties();
                    Debug.Log("Capa 'Ground' creada exitosamente.");
                    break;
                }
            }
        }
        else
        {
            Debug.Log("La capa 'Ground' ya existe.");
        }
    }
} 