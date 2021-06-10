### Quiz 2 DAA (D) Sudoku6x6-DFS
# HOW IT WORKS

## Core Elements

To make it easier to understand, we will visualize the algorithm through the following image:
![Visualisasi 1](https://user-images.githubusercontent.com/57068224/121516669-b0d97800-ca18-11eb-9e29-e47e7e8cae12.png)

Dalam program ini terdapat 2 elemen inti. **Elemen pertama disimbolkan oleh graph** yang berarti **probabilitas gerakan-gerakan yang bisa dilakukan dalam sudoku**.
Gerakan-gerakan tersebut juga dibedakan dengan **warna hijau yang berarti gerakan valid dan oranye yang berarti tidak Valid**. **Elemen Kedua adalah stack** yang bertugas untuk
**menyimpan pergerakan-pergerakan sehingga mudah untuk backtracking**.

## Langkah-langkah program

1. Program akan menelusuri probabilitas-probabilitas pergerakan memungkinkan yang dipetakan menjadi Graph. Selain itu, pergerakan-pergerakannya disimpan ke stack.
![Visualisasi 2](https://user-images.githubusercontent.com/57068224/121516684-b5059580-ca18-11eb-93df-8ba7133e0269.png)
2. Dikarenakan program ini menggunakan algoritma DFS sehingga pergerakan selanjutnya adalah mencari anak dari parent B. C dimasukkan kedalam Stack.
![Visualisasi 3](https://user-images.githubusercontent.com/57068224/121516894-f138f600-ca18-11eb-9186-cf0836ed8563.png)
3. Since C is invalid, the program performs backtracking assisted by the stack. In the stack, C is removed so that the program will look for another child of B other than 
![Visualisasi 4](https://user-images.githubusercontent.com/57068224/121516905-f39b5000-ca18-11eb-81f0-117f707d6604.png)
4. After that, the program moves forward to node F. Node F is proven valid so that the program continues its movement to node G.
![Visualisasi 5](https://user-images.githubusercontent.com/57068224/121516925-f72ed700-ca18-11eb-9b06-d0c87921f349.png)
5. Since node G is the last step that completes sudoku, the DFS process is terminated. After that, the program displays output in the form of the contents of Node G.
