#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

//methods
int count_letters(string text);
int count_words(string text);
int count_sentances(string text);

//index = 0.0588 * L - 0.296 * S - 15.8

int main(void)
{

    //getting text from user
    string text = get_string("Text: ");

    //getting letters in text
    int letters = count_letters(text);

    //getting words in text
    int words = count_words(text);

    //getting sentances in text
    int sentances = count_sentances(text);


    float L = (float)letters / words * 100.0;
    float S = (float)sentances / words * 100.0;

    int grade = round(0.0588 * L - 0.296 * S - 15.8);

    //rounding to nearest int
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

int count_letters(string text)
{
    int letters = 0;
    for (int i = 0, l = strlen(text); i < l ; i++)
    {
        if ((text[i] >= 97 && text[i] <= 122) || (text[i] >= 65 && text[i] <= 90))
        {
            letters++;
        }
    }
    return letters;
}

int count_words(string text)
{
    int words = 0;
    for (int i = 0, l = strlen(text); i < l ; i++)
    {
        if ((text[i] != 32 && text[i + 1] == 32) || (text[i] != 32 && text[i + 1] == 0))
        {
            words++;
        }
    }
    return words;
}

int count_sentances(string text)
{
    int sentances = 0;
    for (int i = 0, l = strlen(text); i < l ; i++)
    {
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            sentances++;
        }
    }
    return sentances;
}