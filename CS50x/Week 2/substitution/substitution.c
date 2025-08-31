#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

string substitute(string ptext, string argv[]);

int main(int argc, string argv[])
{
    //error check for command-line arguments
    if (argc != 2)
    {
        printf("Incorrect number of command-line arguments\n");
        return 1;
    }

    int count = 0;
    //getting length of argv
    while (argv[1][count] != 0)
    {
        count++;
    }

    //checking if argv[1] is 26 characters
    if (count != 26)
    {
        printf("Incorrect number of characters\n");
        return 1;
    }

    //checking if all characters are valid
    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Use only letters\n");
            return 1;
        }
    }

    //changing to all uppercase for ease
    for (int i = 0; i < 26; i++)
    {
        if (islower(argv[1][i]))
        {
            argv[1][i] -= 32;
        }
    }

    //checking for duplicates in the array
    for (int i = 0; i < 26; i ++)
    {
        for (int j = i + 1; j < 26; j++)
        {
            if (argv[1][i] == argv[1][j])
            {
                printf("There are duplicate characters in the key\n");
                return 1;
            }
        }
    }

    //getting plain text
    string ptext = get_string("plaintext:  ");

    string ctext = substitute(ptext, argv);

    //outputting new text
    printf("ciphertext: %s\n", ctext);
}



string substitute(string ptext, string argv[])
{
    string ctext = ptext;
    int spot;
    for (int i = 0, length = strlen(ptext); i < length; i++)
    {
        if (isalpha(ptext[i]))
        {
            if (islower(ptext[i]))
            {
                spot = ptext[i] - 97;
                ctext[i] = argv[1][spot] + 32;
            }
            else
            {
                spot = ptext[i] - 65;
                ctext[i] = argv[1][spot];
            }
        }
        else
        {
            ctext[i] = ptext[i];
        }
    }
    return ctext;
}
