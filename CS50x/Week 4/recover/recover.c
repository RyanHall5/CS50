#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{

    //check arg count
    if (argc!=2)
    {
        printf("Incorrent number of command-line arguments");
        return 1;
    }

    //open file
    FILE *inFile = fopen(argv[1], "r");

    //check if file exists
    if(inFile==NULL)
    {
        printf("File can not be opened");
        return 2;
    }



    //buffer array
    unsigned char buffer[512];

    //number of images counted
    int count = 0;

    //output file
    FILE *outFile = NULL;

    //char filename[8]
    char *filename = malloc(8 * sizeof(char));


    // read 512 byte blocks
    while(fread(buffer, sizeof(char), 512, inFile))
    {
        if(buffer[0]==0xff && buffer[1]==0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (count > 0)
            {
                fclose(outFile);
            }
            //file names
            sprintf( filename, "%03i.jpg", count);
            //open outfile
            outFile = fopen(filename,"w");
            //increase count
            count++;
        }
        if(outFile!=NULL)
        {
            fwrite(buffer, sizeof(char), 512, outFile);
        }
    }
    free (filename);
    fclose(outFile);
    fclose(inFile);

    return 0;

}