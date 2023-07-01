#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * rawCode;
char * ProcessedCode;
int CharCount = 1000;
int GetCode(char filename[]);
void SplitToInstructions(char *bits);


int main(int argc, char *argv[]) 
{
    char b[CharCount];
    rawCode = &b;
    char a[5][CharCount / 5];
    ProcessedCode = &a;

    GetCode(argv[1]);
    SplitToInstructions(rawCode);

   

    for (int i = 0; i < CharCount; i++)
    {
        printf("%s \n",ProcessedCode[i]);
    }
    
}
int GetCode(char filename[])
{
    FILE *file = fopen(filename, "r");
    if (file) {
        CharCount = fread(rawCode, sizeof(char), 1000, file);
        fclose(file);
    }

   
    
}
void SplitToInstructions(char *bits)
{

    //god i need to learn actual C at some point
    for (int i = 0; i < CharCount; i += 5)
    {
        //printf("%c - %c - %c - %c - %c \n", bits[0+i],bits[1+i],bits[2+i],bits[3+i],bits[4+i]);
        ProcessedCode[i / 5] = bits[i + 0];
        ProcessedCode[i / 5] = bits[i + 1]; 
        ProcessedCode[i / 5] = bits[i + 2]; 
        ProcessedCode[i / 5] = bits[i + 3]; 
        ProcessedCode[i / 5] = bits[i + 4];
        //printf("%c - %c - %c - %c - %c \n", ProcessedCode[i/5][0], ProcessedCode[i/5][1], ProcessedCode[i/5][2], ProcessedCode[i/5][3], ProcessedCode[i/5][4]);    
    }
    return;
    
    
}
