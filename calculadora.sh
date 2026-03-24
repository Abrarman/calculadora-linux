#!/bin/bash

echo "Calculadora Lógica (Shell Script)"

while true; do
  echo "Digite o primeiro número:"
  read num1

  echo "Digite o segundo número:"
  read num2

  echo ""
  echo "Escolha a operação:"
  echo "1 - Soma"
  echo "2 - Subtração"
  echo "3 - Multiplicação"
  echo "4 - Divisão"
  echo "5 - Potência"
  echo "6 - Comparação"
  echo "7 - Paridade"
  echo "8 - Sair"

  read escolha

  case $escolha in
    1) echo "Resultado: $((num1 + num2))" ;;
    2) echo "Resultado: $((num1 - num2))" ;;
    3) echo "Resultado: $((num1 * num2))" ;;
    4)
       if [ $num2 -ne 0 ]; then
         echo "Resultado: $((num1 / num2))"
       else
         echo "Erro: divisão por zero!"
       fi ;;
    5) echo "Resultado: $((num1 ** num2))" ;;
    6)
       if [ $num1 -gt $num2 ]; then
         echo "$num1 é maior e $num2 é menor"
       elif [ $num1 -lt $num2 ]; then
         echo "$num1 é menor e $num2 é maior"
       else
         echo "$num1 e $num2 são iguais"
       fi ;;
    7)
       if [ $((num1 % 2)) -eq 0 ]; then
         echo "$num1 é par"
       else
         echo "$num1 é ímpar"
       fi

       if [ $((num2 % 2)) -eq 0 ]; then
         echo "$num2 é par"
       else
         echo "$num2 é ímpar"
       fi ;;
    8)
       echo "Encerrando. Bons estudos!"
       break ;;
    *)
       echo "Opção inválida." ;;
  esac

  echo ""
  echo "Deseja continuar? (s/n)"
  read continuar
  [ "$continuar" != "s" ] && break
done
