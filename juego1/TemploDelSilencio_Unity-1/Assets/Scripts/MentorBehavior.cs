
using UnityEngine;

public class MentorBehavior : MonoBehaviour
{
    public string mentorName = "Shen-Ra";
    public string[] wisdomPhrases;

    void Start()
    {
        SpeakWisdom();
    }

    public void SpeakWisdom()
    {
        if (wisdomPhrases.Length > 0)
        {
            int index = Random.Range(0, wisdomPhrases.Length);
            Debug.Log(mentorName + " dice: " + wisdomPhrases[index]);
        }
    }
}
