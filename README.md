### Quiz 2 DAA (D) Sudoku6x6-DFS
# HOW IT WORKS

## Elemen-elemen penting

Agar lebih mudah dipahami, kami akan memvisualisasikan algoritmanya melalui gambar berikut :
![Visualisasi 1](https://user-images.githubusercontent.com/57068224/121516669-b0d97800-ca18-11eb-9e29-e47e7e8cae12.png)

Dalam program ini terdapat 2 elemen inti. **Elemen pertama disimbolkan oleh graph** yang berarti **probabilitas gerakan-gerakan yang bisa dilakukan dalam sudoku**.
Gerakan-gerakan tersebut juga dibedakan dengan **warna hijau yang berarti gerakan valid dan oranye yang berarti tidak Valid**. **Elemen Kedua adalah stack** yang bertugas untuk
**menyimpan pergerakan-pergerakan sehingga mudah untuk backtracking**.

## Langkah-langkah program

1. Program akan menelusuri probabilitas-probabilitas pergerakan memungkinkan yang dipetakan menjadi Graph. Selain itu, pergerakan-pergerakannya disimpan ke stack.
![Visualisasi 2](https://user-images.githubusercontent.com/57068224/121516684-b5059580-ca18-11eb-93df-8ba7133e0269.png)
2. Dikarenakan program ini menggunakan algoritma DFS sehingga pergerakan selanjutnya adalah mencari anak dari parent B. C dimasukkan kedalam Stack.
![Visualisasi 3](https://user-images.githubusercontent.com/57068224/121516894-f138f600-ca18-11eb-9186-cf0836ed8563.png)
3. Dikarenakan C tidak valid, program melakukan backtracking yang dibantu oleh stack. Dalam stack, C dikeluarkan sehingga program akan mencari lagi child dari B selain C.
![Visualisasi 4](https://user-images.githubusercontent.com/57068224/121516905-f39b5000-ca18-11eb-81f0-117f707d6604.png)
4. Setelah itu, program bergerak maju ke node F. Node F dibuktikan valid sehingga program melanjutkan pergerakannya ke node G.
![Visualisasi 5](https://user-images.githubusercontent.com/57068224/121516925-f72ed700-ca18-11eb-9b06-d0c87921f349.png)
5. Dikarenakan node G merupakan langkah terakhir yang membuat sudoku lengkap, proses DFS diberhentikan. Setelah itu, Program menampilkan output yang berupa isi dari Node G.
