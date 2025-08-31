#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //initializing
    int height;
    string block="";
    //getting height from user
    do
    {
        height=get_int("Height: ");
    }while(height<1 );


    //printing pyramids
    for(int i=1;i<=height;i++)
    {
        //loop for first staircase
        for(int j=height;j>0;j--)
        {
            if(j>i)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        //space between staircases
        printf("  ");

        for(int k=0;k<height;k++){

            if(k<i)
            {
                printf("#");
            }
        }
        printf("\n");



    }

}