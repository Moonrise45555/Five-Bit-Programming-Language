#include <stdio.h>
#define MAX_SIZE 1000
char rawCode[MAX_SIZE];
int GetCode(char filename[]);
int main(int argc, char *argv[]) 
{

    GetCode(argv[1]);
    for (int i = 0; i < MAX_SIZE; i++)
    {
        printf("%s \n",SplitToInstructions(&rawCode[i]));
    }
    
}
int GetCode(char filename[])
{
    char buffer[MAX_SIZE];


   
    FILE *file = fopen(filename, "r");

    if (file == NULL) {
        printf("Unable to open the file.\n");
        return 1;
    }

    
    while (fgets(rawCode, MAX_SIZE, file) != NULL) {
    }

    fclose(file);

    return 0;
}
void SplitToInstructions(char bits[])
{

    //pretty inefficient as it uses MAX_SIZE as a constant size, but speed isnt really a concern right now
    char instructs[5][MAX_SIZE];
    for (int i = 0; i < MAX_SIZE; i += 5)
    {

        instructs[i / 5][0] = bits[i + 0];
        instructs[i / 5][1] = bits[i + 1]; 
        instructs[i / 5][2] = bits[i + 2]; 
        instructs[i / 5][3] = bits[i + 3]; 
        instructs[i / 5][4] = bits[i + 4];    
    }
    &rawCode = instructs;
    
}
