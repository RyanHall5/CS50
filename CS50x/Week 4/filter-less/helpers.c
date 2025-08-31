#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float avg = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed)/3.0;
            image[i][j].rgbtRed = (int)round(avg);
            image[i][j].rgbtGreen = (int)round(avg);
            image[i][j].rgbtBlue = (int)round(avg);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepiaRed = (int)round((.393 * image[i][j].rgbtRed) + (.769 * image[i][j].rgbtGreen) + (.189 * image[i][j].rgbtBlue));
            int sepiaGreen = (int)round((.349 * image[i][j].rgbtRed) + (.686 * image[i][j].rgbtGreen) + (.168 * image[i][j].rgbtBlue));
            int sepiaBlue = (int)round((.272 * image[i][j].rgbtRed) + (.534 * image[i][j].rgbtGreen) + (.131 * image[i][j].rgbtBlue));
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];


    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            temp[i][j] = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp[i][j];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    //making a copy of the image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j].rgbtRed = image[i][j].rgbtRed;
            copy[i][j].rgbtGreen = image[i][j].rgbtGreen;
            copy[i][j].rgbtBlue = image[i][j].rgbtBlue;
        }
    }


    //blurring
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if(i==0 && j==0)//top left corner
            {
                image[i][j].rgbtRed=round((copy[i][j].rgbtRed + copy[i][j+1].rgbtRed + copy[i+1][j].rgbtRed + copy[i+1][j+1].rgbtRed)/4.0);
                image[i][j].rgbtGreen=round((copy[i][j].rgbtGreen + copy[i][j+1].rgbtGreen + copy[i+1][j].rgbtGreen + copy[i+1][j+1].rgbtGreen)/4.0);
                image[i][j].rgbtBlue=round((copy[i][j].rgbtBlue + copy[i][j+1].rgbtBlue + copy[i+1][j].rgbtBlue + copy[i+1][j+1].rgbtBlue)/4.0);
            }
            else if(i==0 && j!=0 && j!=width-1)//top edge
            {
                image[i][j].rgbtRed=round((copy[i][j-1].rgbtRed + copy[i][j].rgbtRed + copy[i][j+1].rgbtRed + copy[i+1][j-1].rgbtRed + copy[i+1][j].rgbtRed + copy[i+1][j+1].rgbtRed)/6.0);
                image[i][j].rgbtGreen=round((copy[i][j-1].rgbtGreen + copy[i][j].rgbtGreen + copy[i][j+1].rgbtGreen + copy[i+1][j-1].rgbtGreen + copy[i+1][j].rgbtGreen + copy[i+1][j+1].rgbtGreen)/6.0);
                image[i][j].rgbtBlue=round((copy[i][j-1].rgbtBlue + copy[i][j].rgbtBlue + copy[i][j+1].rgbtBlue + copy[i+1][j-1].rgbtBlue + copy[i+1][j].rgbtBlue + copy[i+1][j+1].rgbtBlue)/6.0);
            }
            else if(i==0 && j==width-1)//top right corner
            {
                image[i][j].rgbtRed=round((copy[i][j-1].rgbtRed + copy[i][j].rgbtRed + copy[i+1][j-1].rgbtRed + copy[i+1][j].rgbtRed)/4.0);
                image[i][j].rgbtGreen=round((copy[i][j-1].rgbtGreen + copy[i][j].rgbtGreen + copy[i+1][j-1].rgbtGreen + copy[i+1][j].rgbtGreen)/4.0);
                image[i][j].rgbtBlue=round((copy[i][j-1].rgbtBlue + copy[i][j].rgbtBlue + copy[i+1][j-1].rgbtBlue + copy[i+1][j].rgbtBlue)/4.0);
            }
            else if(i!=0 && i!=height-1 && j==0)//left edge
            {
                image[i][j].rgbtRed=round((copy[i-1][j].rgbtRed + copy[i-1][j+1].rgbtRed + copy[i][j].rgbtRed + copy[i][j+1].rgbtRed + copy[i+1][j].rgbtRed + copy[i+1][j+1].rgbtRed)/6.0);
                image[i][j].rgbtGreen=round((copy[i-1][j].rgbtGreen + copy[i-1][j+1].rgbtGreen + copy[i][j].rgbtGreen + copy[i][j+1].rgbtGreen + copy[i+1][j].rgbtGreen + copy[i+1][j+1].rgbtGreen)/6.0);
                image[i][j].rgbtBlue=round((copy[i-1][j].rgbtBlue + copy[i-1][j+1].rgbtBlue + copy[i][j].rgbtBlue + copy[i][j+1].rgbtBlue + copy[i+1][j].rgbtBlue + copy[i+1][j+1].rgbtBlue)/6.0);
            }
            else if(i!=0 && i!=height-1 && j==width-1)//right edge
            {
                image[i][j].rgbtRed=round((copy[i-1][j-1].rgbtRed + copy[i-1][j].rgbtRed + copy[i][j-1].rgbtRed + copy[i][j].rgbtRed + copy[i+1][j-1].rgbtRed + copy[i+1][j].rgbtRed)/6.0);
                image[i][j].rgbtGreen=round((copy[i-1][j-1].rgbtGreen + copy[i-1][j].rgbtGreen + copy[i][j-1].rgbtGreen + copy[i][j].rgbtGreen + copy[i+1][j-1].rgbtGreen + copy[i+1][j].rgbtGreen)/6.0);
                image[i][j].rgbtBlue=round((copy[i-1][j-1].rgbtBlue + copy[i-1][j].rgbtBlue + copy[i][j-1].rgbtBlue + copy[i][j].rgbtBlue + copy[i+1][j-1].rgbtBlue + copy[i+1][j].rgbtBlue)/6.0);
            }
            else if(i==height-1 && j==0)//bottom left corner
            {
                image[i][j].rgbtRed=round((copy[i-1][j].rgbtRed + copy[i-1][j+1].rgbtRed + copy[i][j].rgbtRed + copy[i][j+1].rgbtRed)/4.0);
                image[i][j].rgbtGreen=round((copy[i-1][j].rgbtGreen + copy[i-1][j+1].rgbtGreen + copy[i][j].rgbtGreen + copy[i][j+1].rgbtGreen)/4.0);
                image[i][j].rgbtBlue=round((copy[i-1][j].rgbtBlue + copy[i-1][j+1].rgbtBlue + copy[i][j].rgbtBlue + copy[i][j+1].rgbtBlue)/4.0);
            }
            else if(i==height-1 && j!=0 && j!=width-1)//bottom edge
            {
                image[i][j].rgbtRed=round((copy[i-1][j-1].rgbtRed + copy[i-1][j].rgbtRed + copy[i-1][j+1].rgbtRed + copy[i][j-1].rgbtRed + copy[i][j].rgbtRed + copy[i][j+1].rgbtRed)/6.0);
                image[i][j].rgbtGreen=round((copy[i-1][j-1].rgbtGreen + copy[i-1][j].rgbtGreen + copy[i-1][j+1].rgbtGreen + copy[i][j-1].rgbtGreen + copy[i][j].rgbtGreen + copy[i][j+1].rgbtGreen)/6.0);
                image[i][j].rgbtBlue=round((copy[i-1][j-1].rgbtBlue + copy[i-1][j].rgbtBlue + copy[i-1][j+1].rgbtBlue + copy[i][j-1].rgbtBlue + copy[i][j].rgbtBlue + copy[i][j+1].rgbtBlue)/6.0);
            }
            else if(i==height-1 && j==width-1)//bottom right corner
            {
                image[i][j].rgbtRed=round((copy[i-1][j-1].rgbtRed + copy[i-1][j].rgbtRed + copy[i][j-1].rgbtRed + copy[i][j].rgbtRed)/4.0);
                image[i][j].rgbtGreen=round((copy[i-1][j-1].rgbtGreen + copy[i-1][j].rgbtGreen + copy[i][j-1].rgbtGreen + copy[i][j].rgbtGreen)/4.0);
                image[i][j].rgbtBlue=round((copy[i-1][j-1].rgbtBlue + copy[i-1][j].rgbtBlue + copy[i][j-1].rgbtBlue + copy[i][j].rgbtBlue)/4.0);
            }
            else//not on edge
            {
                image[i][j].rgbtRed=round((copy[i-1][j-1].rgbtRed + copy[i-1][j].rgbtRed + copy[i-1][j+1].rgbtRed + copy[i][j-1].rgbtRed + copy[i][j].rgbtRed + copy[i][j+1].rgbtRed + copy[i+1][j-1].rgbtRed + copy[i+1][j].rgbtRed + copy[i+1][j+1].rgbtRed)/9.0);
                image[i][j].rgbtGreen=round((copy[i-1][j-1].rgbtGreen + copy[i-1][j].rgbtGreen + copy[i-1][j+1].rgbtGreen + copy[i][j-1].rgbtGreen + copy[i][j].rgbtGreen + copy[i][j+1].rgbtGreen + copy[i+1][j-1].rgbtGreen + copy[i+1][j].rgbtGreen + copy[i+1][j+1].rgbtGreen)/9.0);
                image[i][j].rgbtBlue=round((copy[i-1][j-1].rgbtBlue + copy[i-1][j].rgbtBlue + copy[i-1][j+1].rgbtBlue + copy[i][j-1].rgbtBlue + copy[i][j].rgbtBlue + copy[i][j+1].rgbtBlue + copy[i+1][j-1].rgbtBlue + copy[i+1][j].rgbtBlue + copy[i+1][j+1].rgbtBlue)/9.0);
            }
        }
    }
    return;
}
