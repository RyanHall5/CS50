#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int year=0, born, died,sPop,ePop;
    do
    {
    sPop = get_int("Start size: ");
    }while(sPop<9);

    do
    {
    ePop = get_int("End size: ");
    }while(ePop<sPop);


    
    while(sPop<ePop)
    {
        born=sPop/3;
        died=sPop/4;
        sPop=sPop+born-died;
        year++;
    }

    printf("Years: %i\n", year);

}