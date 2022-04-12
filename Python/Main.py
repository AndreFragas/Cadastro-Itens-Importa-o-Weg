from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from typing import Sized
from numpy import string_
from openpyxl import *
import pandas as pd
from PIL import ImageTk, Image

janela = Tk()
RuasDisponiveis = []
Bloqueados = []
rConsultaNumero = StringVar()
rConsultaDescricao = StringVar()
rConsultaPeso = StringVar()
rConsultaAltura = StringVar()
rConsultaLargura = StringVar()
rConsultaComprimento = StringVar()
rRuasDisponiveis = StringVar()
rRuasDisponiveis2 = StringVar()
rRuasDisponiveis3 = StringVar()

class validadores:
    def validadorOitoDigitosNumericos(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100000000
    def validadorQuatroDigitosNumericos(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 10000
    def validadorDoisDigitosNumericos(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100
class Funcs():
    def chamarAnalise(self):
        #Esconde todos os frames que estão visiveis atualmente
        self.esconderFrames()
        #Mostra o frame na tela com todos os seus objetos
        self.frame1.place(relx=0.02, rely=0.03, relheight=0.46, relwidth=0.96)
    def chamarBloqueado(self):
        #Esconde todos os frames que estão visiveis atualmente
        self.esconderFrames()
        #Mostra o frame na tela com todos os seus objetos
        self.frame2.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    def chamarConsulta(self):
        #Esconde todos os frames que estão visiveis atualmente
        self.esconderFrames()
        #Mostra o frame na tela com todos os seus objetos
        self.frame3.place(relx=0.02, rely=0.03, relheight=0.46, relwidth=0.96)
    def chamarCriarItem(self):
        #Esconde todos os frames que estão visiveis atualmente
        self.esconderFrames()
        #Mostra o frame na tela com todos os seus objetos
        self.frame4.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    def chamarEditarItem(self):
        #Esconde todos os frames que estão visiveis atualmente
        self.esconderFrames()
        #Mostra o frame na tela com todos os seus objetos
        self.frame5.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    def chamarCriarRuas(self):
        #Esconde todos os frames que estão visiveis atualmente
        self.esconderFrames()
        #Mostra o frame na tela com todos os seus objetos
        self.frame6.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    def chamarEditarRuas(self):
        #Esconde todos os frames que estão visiveis atualmente
        self.esconderFrames()
        #Mostra o frame na tela com todos os seus objetos
        self.frame7.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    def esconderFrames(self):
        #Comando para deixar o frame invisivel
        self.frame1.place_forget()
        self.frame1_1.place_forget()
        self.frame2.place_forget()
        self.frame3.place_forget()
        self.frame3_1.place_forget()
        self.frame3_2.place_forget()
        self.frame4.place_forget()
        self.frame5.place_forget()
        self.frame6.place_forget()
        self.frame7.place_forget()
    def verificarDisponibilidade(self):
        self.txtErroCampoVazio = "Algum campo de dado está vázio, por favor preencha todos os campos!"
        if self.vitemF1.get() == "":
            messagebox.showerror(title="Campo Vazio", message=self.txtErroCampoVazio)
            return
        #Realiza a leitura dos dados do Excel
        self.df = pd.read_excel(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", sheet_name="Itens", usecols=[1,2,3,4,5,6])
        self.df2 = pd.read_excel(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", sheet_name="Ruas", usecols=[1,2,3,4,5,6])
        self.writer = pd.ExcelWriter(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", engine='xlsxwriter')
        #Define o modelo de apresentação de dados de retorno ao usuário
        self.txtBloqueado = "O item {0} foi adicionado ao estoque bloqueado!"
        self.txtDisponiveis = "As ruas que suportam o armazenamento do material são: {0}"
        self.txtErro1 = "O item {0} não está cadastrado no sistema ou foi digitado de forma incorreta!"
        #Recebe os dados do usuário
        self.i1 = self.vitemF1.get()
        self.i = int(self.i1)
        #Contadores utilizados na verificação de dados!
        contadorDeItens = self.df.shape[0]
        contador = 0
        #Verifica se o item está presente no banco de dados!
        for item in self.df['Item']:
            if item == self.i:
                break
            else:
                contador += 1
            if contadorDeItens == contador:
                messagebox.showerror(title="Erro de cadastro!",message=self.txtErro1.format(self.i))
                self.df.to_excel(self.writer, sheet_name="Itens")
                self.df2.to_excel(self.writer, sheet_name="Ruas")
                self.writer.save()
                self.limparTela()
                return
        #Realiza busca de cada dado através da entrada do usuário e armazena na variavel
        self.linha = self.df.loc[self.df['Item'] == self.i]
        self.peso = self.linha.iloc[0, 2]
        self.altura = self.linha.iloc[0, 3]
        self.largura = self.linha.iloc[0, 5]
        self.comprimento = self.linha.iloc[0, 4]
        #Percorre por todos os dados da coluna Rua do Excel
        for rua in self.df2['Rua']:
            #Verifica se a rua procurada é igual a que o laço está buscando e adiciona os dados da linha nas variaveis 
            self.linhaRua = self.df2.loc[self.df2['Rua'] == rua]
            self.pesoMaximo = self.linhaRua.iloc[0, 1]
            self.alturaMaxima = self.linhaRua.iloc[0, 2]
            self.larguraMaxima = self.linhaRua.iloc[0, 4]
            self.comprimentoMaximo = self.linhaRua.iloc[0, 3]
            #Verifica se a rua suporta cada dimensão do item
            if self.peso <= self.pesoMaximo:
                if self.altura < self.alturaMaxima:
                    if self.largura < self.larguraMaxima:
                        if self.comprimento < self.comprimentoMaximo:
                            #Caso a rua suporte os dados do item salva o número da rua na lista
                            self.ruaDisponivel = self.linhaRua.iloc[0, 0]
                            RuasDisponiveis.append(self.ruaDisponivel)
        #Verifica se a lista está vazia
        if len(RuasDisponiveis) == 0:
            #Se a lista estiver vazia adiciona o numero do item a lista de bloqueados
            self.bloqueado = self.linha.iloc[0, 0]
            Bloqueados.append(self.bloqueado)
            messagebox.showinfo(title="Estoque Bloqueado", message=self.txtBloqueado.format(self.bloqueado))
        else:
            #Se a lista não estiver vazia mostra a lista de ruas e depois deixa a lista vazia
            self.frame1_1.place_forget()
            self.frame1_1.place(relx=0.02,rely=0.50, relheight=0.47, relwidth=0.96)
            rRuasDisponiveis.set(RuasDisponiveis[0:21])
            rRuasDisponiveis2.set(RuasDisponiveis[21:42])
            rRuasDisponiveis3.set(RuasDisponiveis[42:63])
            RuasDisponiveis.clear()
        #Salva os dados do Excel
        self.df.to_excel(self.writer, sheet_name="Itens")
        self.df2.to_excel(self.writer, sheet_name="Ruas")
        self.writer.save()
        #Limpa os dados de entrada do usuário
        self.limparTela()
    def limparTela(self):
        #Limpa todos os dados de entrada de usuário
        self.vitemF1.delete(0, END)
        self.vitemF4.delete(0, END)
        self.edadoF3.delete(0, END)
        self.edadoF5.delete(0, END)
        self.edadoF7.delete(0, END)
        self.enumeroF3.delete(0, END)
        self.vdescricaoF4.delete(0, END)
        self.vpesoF4.delete(0, END)
        self.valturaF4.delete(0, END)
        self.vlarguraF4.delete(0, END)
        self.vcomprimentoF4.delete(0, END)
        self.eitemF5.delete(0, END)
        self.novoDadoF5.delete(0, END)
        self.novoDadoF7.delete(0, END)
        self.vruaF6.delete(0, END)
        self.vpesoMaximoF6.delete(0, END)
        self.valturaMaximaF6.delete(0, END)
        self.vlarguraMaximaF6.delete(0, END)
        self.vcomprimentoMaximoF6.delete(0, END)
        self.eruaF7.delete(0, END)
    def realizarConsulta(self):
        self.txtErroCampoVazio = "Algum campo de dado está vázio, por favor preencha todos os campos!"
        if self.enumeroF3.get() == "" or self.edadoF3.get() == "":
            messagebox.showerror(title="Campo Vazio", message=self.txtErroCampoVazio)
            return
        #Realiza a leitura dos dados do Excel
        self.df = pd.read_excel(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", sheet_name="Itens", usecols=[1,2,3,4,5,6])
        self.df2 = pd.read_excel(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", sheet_name="Ruas", usecols=[1,2,3,4,5,6])
        self.writer = pd.ExcelWriter(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", engine='xlsxwriter')
        #Define o modelo de apresentação de dados de retorno ao usuário
        self.txtConsultaItem = "Segue dados do item consultado:\n {0}"
        self.txtConsultaRua = "Segue dados da rua consultada:\n {0}"
        self.txtErroConsultaItem = "O item {0} não consta na nossa base de dados!"
        self.txtErroConsultaRua = "A rua {0} não consta na nossa base de dados!"
        #Recebe os dados do usuário
        self.i1 = self.enumeroF3.get()
        self.i = int(self.i1)
        self.j = self.edadoF3.get()
        contadorDeItens = self.df.shape[0]
        contadorDeRuas = self.df2.shape[0]
        contador = 0
        #Verifica se o usuário selecionou a opção de consulta de Item ou Rua!
        if self.j == "Item":
            self.frame3_1.place(relx=0.02,rely=0.50, relheight=0.47, relwidth=0.96)
            #Verifica a base de dados se ela possui ou não os dados necessários
            for item in self.df['Item']:
                if item == self.i:
                    break
                else:
                    contador += 1
                if contadorDeItens == contador:
                    messagebox.showerror(title="Erro de cadastro!",message=self.txtErroConsultaItem.format(self.i))
                    self.df.to_excel(self.writer, sheet_name="Itens")
                    self.df2.to_excel(self.writer, sheet_name="Ruas")
                    self.writer.save()
                    self.limparTela()
                    return
            #Realiza a consulta e salva na variavel 'consulta'
            consulta = self.df.loc[self.df['Item'] == self.i]
            #Retorna o resultado da pesquisa para o usuário
            self.frame3_2.place_forget()
            self.frame3_1.place(relx=0.02,rely=0.50, relheight=0.47, relwidth=0.96)
            rConsultaNumero.set(consulta.iat[0,0])
            rConsultaDescricao.set(consulta.iat[0,1])
            rConsultaPeso.set(consulta.iat[0,2])
            rConsultaAltura.set(consulta.iat[0,3])
            rConsultaLargura.set(consulta.iat[0,4])
            rConsultaComprimento.set(consulta.iat[0,5])
            #Salva os dados do Excel
            self.df.to_excel(self.writer, sheet_name="Itens")
            self.df2.to_excel(self.writer, sheet_name="Ruas")
            self.writer.save()
            #Limpa o campo de entrada do usuário
            self.enumeroF3.delete(0, END)
        elif self.j == "Rua":
            #Verifica a base de dados se ela possui ou não os dados necessários
            for rua in self.df2['Rua']:
                if rua == self.i:
                    break
                else:
                    contador += 1
                if contadorDeRuas == contador:
                    messagebox.showerror(title="Erro de cadastro!",message=self.txtErroConsultaRua.format(self.i))
                    self.df.to_excel(self.writer, sheet_name="Itens")
                    self.df2.to_excel(self.writer, sheet_name="Ruas")
                    self.writer.save()
                    self.limparTela()
                    return
            #Realiza a consulta e salva na variavel 'consulta'
            consulta = self.df2.loc[self.df2['Rua'] == self.i]
            #Retorna o resultado da pesquisa para o usuário
            self.frame3_1.place_forget()
            self.frame3_2.place(relx=0.02,rely=0.50, relheight=0.47, relwidth=0.96)
            rConsultaNumero.set(consulta.iat[0,0])
            rConsultaPeso.set(consulta.iat[0,1])
            rConsultaAltura.set(consulta.iat[0,2])
            rConsultaLargura.set(consulta.iat[0,3])
            rConsultaComprimento.set(consulta.iat[0,4])
            #Salva os dados do Excel
            self.df.to_excel(self.writer, sheet_name="Itens")
            self.df2.to_excel(self.writer, sheet_name="Ruas")
            self.writer.save()
            #Limpa o campo de entrada do usuário
            self.enumeroF3.delete(0, END)
    def criarItem(self):
        self.txtErroCampoVazio = "Algum campo de dado está vázio, por favor preencha todos os campos!"
        if self.vitemF4.get() == "" or self.vdescricaoF4.get() == "" or self.vpesoF4.get() == "" or self.valturaF4.get() == "" or self.vlarguraF4.get() == "" or self.vcomprimentoF4.get() == "":
            messagebox.showerror(title="Campo Vazio", message=self.txtErroCampoVazio)
            return
        #Realiza a leitura dos dados do Excel
        self.df = pd.read_excel(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", sheet_name="Itens", usecols=[1,2,3,4,5,6])
        self.df2 = pd.read_excel(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", sheet_name="Ruas", usecols=[1,2,3,4,5,6])
        self.writer = pd.ExcelWriter(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", engine='xlsxwriter')
        #Define o modelo de apresentação de dados de retorno ao usuário
        self.txtCriarItem = "Item {0} criado com sucesso!"
        self.txtErroCadastroItem = "O item {0} já possui cadastro"
        #Verifica qual a quantidade de itens cadastrados no Excel e retorna o valor da próxima casa vazia
        contadorDeItens = self.df.shape[0]
        #Recebe a entrada do número do item!
        self.i1 = self.vitemF4.get()
        self.i = int(self.i1)
        #Verifica se o item já possui cadastro!
        for item in self.df['Item']:
            if item == self.i:
                messagebox.showerror(title="Erro de cadastro!",message=self.txtErroCadastroItem.format(self.i))
                self.df.to_excel(self.writer, sheet_name="Itens")
                self.df2.to_excel(self.writer, sheet_name="Ruas")
                self.writer.save()
                self.limparTela()
                return
        #Salva os valores das entradas do usuário na posição especifica na tabela do excel
        self.df.loc[contadorDeItens, "Item"] = self.vitemF4.get()
        self.df.loc[contadorDeItens, "Descrição"] = self.vdescricaoF4.get()
        self.df.loc[contadorDeItens, "Peso"] = self.vpesoF4.get()
        self.df.loc[contadorDeItens, "Altura"] = self.valturaF4.get()
        self.df.loc[contadorDeItens, "Largura"] = self.vlarguraF4.get()
        self.df.loc[contadorDeItens, "Comprimento"] = self.vcomprimentoF4.get()
        #Salva os dados do Excel
        self.df.to_excel(self.writer, sheet_name="Itens")
        self.df2.to_excel(self.writer, sheet_name="Ruas")
        self.writer.save()
        #Imprime que os dados foram cadastrados com sucesso
        messagebox.showinfo(title="Item Criado", message=self.txtCriarItem.format(self.vitemF4.get()))
        #Limpa os dados de entrada do usuário
        self.limparTela()
    def criarRua(self):
        self.txtErroCampoVazio = "Algum campo de dado está vázio, por favor preencha todos os campos!"
        if self.vruaF6.get() == "" or self.vpesoMaximoF6.get() == "" or self.valturaMaximaF6.get() == "" or self.vlarguraMaximaF6.get() == "" or self.vcomprimentoMaximoF6.get() == "":
            messagebox.showerror(title="Campo Vazio", message=self.txtErroCampoVazio)
            return
        #Realiza a leitura dos dados do Excel
        self.df = pd.read_excel(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", sheet_name="Itens", usecols=[1,2,3,4,5,6])
        self.df2 = pd.read_excel(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", sheet_name="Ruas", usecols=[1,2,3,4,5,6])
        self.writer = pd.ExcelWriter(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", engine='xlsxwriter')
        #Define o modelo de apresentação de dados de retorno ao usuário
        self.txtCriarRua = "Rua {0} criada com sucesso!"
        self.txtErroCadastroRua = "A rua {0} já possui cadastro!"
        self.i1 = self.vruaF6.get()
        self.i = int(self.i1)
        for rua in self.df2['Rua']:
            if rua == self.i:
                messagebox.showerror(title="Erro de cadastro!",message=self.txtErroCadastroRua.format(self.i))
                self.df.to_excel(self.writer, sheet_name="Itens")
                self.df2.to_excel(self.writer, sheet_name="Ruas")
                self.writer.save()
                self.limparTela()
                return
        #Verifica qual a quantidade de ruas cadastradas no Excel e retorna o valor da próxima casa vazia
        contadorDeRuas = self.df2.shape[0]
        #Salva os valores das entradas do usuário na posição especifica na tabela do excel
        self.df2.loc[contadorDeRuas, "Rua"] = self.vruaF6.get()
        self.df2.loc[contadorDeRuas, "Peso"] = self.vpesoMaximoF6.get()
        self.df2.loc[contadorDeRuas, "Altura"] = self.valturaMaximaF6.get()
        self.df2.loc[contadorDeRuas, "Largura"] = self.vlarguraMaximaF6.get()
        self.df2.loc[contadorDeRuas, "Comprimento"] = self.vcomprimentoMaximoF6.get()
        #Salva os dados do Excel
        self.df.to_excel(self.writer, sheet_name="Itens")
        self.df2.to_excel(self.writer, sheet_name="Ruas")
        self.writer.save()
        #Imprime que os dados foram cadastrados com sucesso
        messagebox.showinfo(title="Rua Criada", message=self.txtCriarRua.format(self.vruaF6.get()))
        #Limpa os dados de entrada do usuário
        self.limparTela()
    def editarItens(self):
        self.txtErroCampoVazio = "Algum campo de dado está vázio, por favor preencha todos os campos!"
        if self.eitemF5.get() == "" or self.edadoF5.get() == "" or self.novoDadoF5 == "":
            messagebox.showerror(title="Campo Vazio", message=self.txtErroCampoVazio)
            return
        #Realiza a leitura dos dados do Excel
        self.df = pd.read_excel(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", sheet_name="Itens", usecols=[1,2,3,4,5,6])
        self.df2 = pd.read_excel(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", sheet_name="Ruas", usecols=[1,2,3,4,5,6])
        self.writer = pd.ExcelWriter(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", engine='xlsxwriter')
        #Mensagem de texto para erros!
        self.txtErroItemSemCadastro = "O item {0} não possui cadastro!"
        #Contadores para verificação!
        contadorDeItens = self.df.shape[0]
        contador = 0
        #Recebe os dados do usuário
        self.i1 = self.eitemF5.get()
        #Altera o tipo de dados para int
        self.i = int(self.i1)
        for item in self.df['Item']:
            if item == self.i:
                break
            else:
                contador += 1
            if contadorDeItens == contador:
                messagebox.showerror(title="Erro de cadastro!",message=self.txtErroItemSemCadastro.format(self.i))
                self.df.to_excel(self.writer, sheet_name="Itens")
                self.df2.to_excel(self.writer, sheet_name="Ruas")
                self.writer.save()
                self.limparTela()
                return
        self.linha = self.df.loc[self.df['Item'] == self.i]                                                                                                                                                                                                                                                                                         
        self.j = self.edadoF5.get()
        #Verifica qual o dado que o usuário deseja editar
        if self.j == 'Descrição':
            #Salva o valor do dado antigo
            self.ant = self.linha.iloc[0, 1]
            #Salva o novo valor para o dado
            self.descricao = self.novoDadoF5.get()
            #Salva o novo valor para o dado na linha e coluna especifica do dado
            self.df.loc[self.df['Item'] == self.i, "Descrição"] = self.descricao
            #Define o modelo de apresentação de dados de retorno ao usuário
            self.txt = "Descrição do item {0} foi alterado de {1} para {2}."
            #Mosta a mensagem de alteração
            messagebox.showinfo(title="Alteração Realizada!", message=self.txt.format(self.i,self.ant,self.descricao))
        elif self.j == 'Peso':                                                                                                      
            self.ant = self.linha.iloc[0, 2]                                                                               
            self.peso = self.novoDadoF5.get()                                               
            self.df.loc[self.df['Item'] == self.i, "Peso"] = self.peso                                                                         
            self.txt = "valor de peso do item {0} foi alterado de {1} para {2}."                                           
            messagebox.showinfo(title="Alteração Realizada!", message=self.txt.format(self.i,self.ant,self.peso))                                                                            
        elif self.j == 'Altura':                                                                                                   
            self.ant = self.linha.iloc[0, 3]                                                                                
            altura = self.novoDadoF5.get()                                             
            self.df.loc[self.df['Item'] == self.i, "Altura"] = self.altura                                                                      
            self.txt = "valor de altura do item {0} foi alterado de {1} para {2}."                                        
            messagebox.showinfo(title="Alteração Realizada!", message=self.txt.format(self.i,self.ant,altura))                                                                          
        elif self.j == 'Largura':                                                                                                    
            self.ant = self.linha.iloc[0, 5]                                                                                 
            self.largura = self.novoDadoF5.get()                                               
            self.df.loc[self.df['Item'] == self.i, "Largura"] = self.largura                                                                          
            self.txt = "valor de largura do item {0} foi alterado de {1} para {2}."                                           
            messagebox.showinfo(title="Alteração Realizada!", message=self.txt.format(self.i,self.ant,self.largura))                                                                             
        elif self.j == 'Comprimento':                                                                                                    
            self.ant = self.linha.iloc[0, 4]                                                                                   
            self.comprimento = self.novoDadoF5.get()                                            
            self.df.loc[self.df['Item'] == self.i, "Comprimento"] == self.comprimento                                                                     
            self.txt = "valor de comprimento do item {0} foi alterado de {1} para {2}."                                      
            messagebox.showinfo(title="Alteração Realizada!", message=self.txt.format(self.i,self.ant,self.comprimento))
        #Salva os dados do Excel                                                                                                                                                                         
        self.df.to_excel(self.writer, sheet_name="Itens")
        self.df2.to_excel(self.writer, sheet_name="Ruas")
        self.writer.save()
        #Limpa os dados de entrada do usuário
        self.limparTela()
    def editarRuas(self):
        self.txtErroCampoVazio = "Algum campo de dado está vázio, por favor preencha todos os campos!"
        if self.eruaF7.get() == "" or self.edadoF7.get() == "" or self.novoDadoF7.get() == "":
            messagebox.showerror(title="Campo Vazio", message=self.txtErroCampoVazio)
            return
        #Realiza a leitura dos dados do Excel
        self.df = pd.read_excel(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", sheet_name="Itens", usecols=[1,2,3,4,5,6])
        self.df2 = pd.read_excel(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", sheet_name="Ruas", usecols=[1,2,3,4,5,6])
        self.writer = pd.ExcelWriter(r"C:\Users\afragas\Desktop\Projeto Solar\Python\assets\dados.xlsx", engine='xlsxwriter')
        #Mensagem de texto para erros!
        self.txtErroRuaSemCadastro = "A rua {0} não possui cadastro!"
        #Contadores para verificação!
        contadorDeRuas = self.df2.shape[0]
        contador = 0
        #Recebe os dados do usuário
        self.i1 = self.eruaF7.get()
        #Altera o tipo de dado para int
        self.i = int(self.i1)
        for rua in self.df2['Rua']:
            if rua == self.i:
                break
            else:
                contador += 1
            if contadorDeRuas == contador:
                messagebox.showerror(title="Erro de cadastro!",message=self.txtErroRuaSemCadastro.format(self.i))
                self.df.to_excel(self.writer, sheet_name="Itens")
                self.df2.to_excel(self.writer, sheet_name="Ruas")
                self.writer.save()
                self.limparTela()
                return
        self.linha = self.df2.loc[self.df2['Rua'] == self.i]
        self.j = self.edadoF7.get()
        #Verifica qual o dado que o usuário deseja editar
        if self.j == 'Peso Máximo':
            #Salva o valor do dado antigo
            self.ant = self.linha.iloc[0, 1]
            #Salva o novo valor para o dado
            self.pesoMaximo = self.novoDadoF7.get()
            #Salva o novo valor para o dado na linha e coluna especifica do dado
            self.df2.loc[self.df2['Rua'] == self.i, "Peso"] = self.pesoMaximo
            #Define o modelo de apresentação de dados de retorno ao usuário
            self.txt = "Valor de máximo suportado da rua {0} foi alterado de {1} para {2}."
            #Mostra a mensagem de alteração
            messagebox.showinfo(title="Alteração Realizada", message=self.txt.format(self.i,self.ant,self.pesoMaximo))
        elif self.j == 'Altura Máxima':
            self.ant = self.linha.iloc[0, 2]
            self.alturaMaxima = self.novoDadoF7.get()
            self.df2.loc[self.df2['Rua'] == self.i, "Altura"] = self.alturaMaxima
            self.txt = "valor de altura máxima da rua {0} foi alterado de {1} para {2}."
            messagebox.showinfo(title="Alteração Realizada", message=self.txt.format(self.i,self.ant,self.alturaMaxima))
        elif self.j == 'Largura Máxima':                                                                                                      
            self.ant = self.linha.iloc[0, 4]                                                                           
            self.larguraMaxima = self.novoDadoF7.get()                                                
            self.df2.loc[self.df2['Rua'] == self.i, "Largura"] = self.larguraMaxima                                                                    
            self.txt = "valor de largura máxima da rua {0} foi alterado de {1} para {2}."                                        
            messagebox.showinfo(title="Alteração Realizada", message=self.txt.format(self.i,self.ant,self.larguraMaxima))                                                                    
        elif self.j == 'Comprimento Máximo':                                                                                                     
            self.ant = self.linha.iloc[0, 3]                                                                              
            self.comprimentoMaximo = self.novoDadoF7.get()                                            
            self.df2.loc[self.df2['Rua'] == self.i, "Comprimento"] = self.comprimentoMaximo                                                                  
            self.txt = "valor de comprimento máximo da rua {0} foi alterado de {1} para {2}."                                    
            messagebox.showinfo(title="Alteração Realizada", message=self.txt.format(self.i,self.ant,self.comprimentoMaximo))
        #Salva os dados do Excel                                                                                                                                                                                                                                                  
        self.df.to_excel(self.writer, sheet_name="Itens")
        self.df2.to_excel(self.writer, sheet_name="Ruas")
        self.writer.save()
        #Limpa os dados de entrada do usuário
        self.limparTela()
class Aplicacao(Funcs, validadores):
    def __init__(self):
        self.janela = janela
        self.validaEntradas()
        self.tela()
        self.frames_da_tela()
        self.chamarAnalise()
        self.chamarBloqueado()
        self.chamarConsulta()
        self.chamarCriarItem()
        self.chamarEditarItem()
        self.chamarCriarRuas()
        self.chamarEditarRuas()
        self.objetosDosFrames()
        self.esconderFrames()
        self.limparTela()
        janela.mainloop()
    def tela(self):
        #Personalização da janela!
        self.janela.title("Weg Solar")
        self.janela.geometry("500x350")
        self.janela.configure(background='#1e3743')
        self.janela.resizable(False, False)
        janela.iconbitmap(r'C:\\Users\\afragas\\Desktop\\Projeto Solar\\Python\\assets\\weg-logo.ico')
        self.imgWeg = ImageTk.PhotoImage(Image.open("C:\\Users\\afragas\\Desktop\\Projeto Solar\\Python\\assets\\weg-logo-256.1.png"))
        self.labelWeg = Label(image=self.imgWeg, border=0, background='#1e3743')
        self.labelWeg.place(x=125, y=35)
        #Criação da barra de menu
        barraDeMenus = Menu(janela)
        menuConsultas = Menu(barraDeMenus, tearoff = 0)
        menuConsultas.add_command(label="Analizar item por rua", command=self.chamarAnalise)
        menuConsultas.add_command(label="Consultar estoque bloqueado", command=self.chamarBloqueado)
        menuConsultas.add_command(label="Consultar Itens/Ruas", command=self.chamarConsulta)
        barraDeMenus.add_cascade(label="Consultas", menu=menuConsultas)
        menuItens = Menu(barraDeMenus, tearoff=0)
        menuItens.add_command(label="Criar Item", command=self.chamarCriarItem)
        menuItens.add_command(label="Editar Item", command=self.chamarEditarItem)
        barraDeMenus.add_cascade(label="Itens", menu=menuItens)
        menuRuas = Menu(barraDeMenus, tearoff=0)
        menuRuas.add_command(label="Criar Rua", command=self.chamarCriarRuas)
        menuRuas.add_command(label="Editar Rua", command=self.chamarEditarRuas)
        barraDeMenus.add_cascade(label="Ruas", menu=menuRuas)
        janela.config(menu=barraDeMenus)
    def frames_da_tela(self):
        #Criação dos frames para cada tela
        #Frame de Analise de Item por Rua
        self.frame1 = Frame(self.janela, border = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        #Frame de mostrar analise do Item
        self.frame1_1 = Frame(self.janela, border = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        #Frame de consulta de Bloqueados
        self.frame2 = Frame(self.janela, border = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        #Frame de consulta de Itens e Ruas
        self.frame3 = Frame(self.janela, border = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        #Frame de mostrar consulta Item
        self.frame3_1 = Frame(self.janela, border = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        #Frame de mostrar consulta Rua
        self.frame3_2 = Frame(self.janela, border = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        #Frame de criação de Itens
        self.frame4 = Frame(self.janela, border = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        #Frame de edição de Itens
        self.frame5 = Frame(self.janela, border = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        #Frame de criação de Ruas
        self.frame6 = Frame(self.janela, border = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        #Frame de edição de Itens
        self.frame7 = Frame(self.janela, border = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
    def objetosDosFrames(self):
        #Objetos do Frame1
        self.label1F1 = Label(self.frame1, text="Item do Material", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2')
        self.label1F1.place(x=175, y=20, width=120, height=20)
        self.vitemF1 = Entry(self.frame1, bd=2, validate="key", validatecommand=self.verificaVitemF1)
        self.vitemF1.place(x=175, y=40, width=120, height=20)
        self.btnAnalizarF1 = Button(self.frame1, text="Analizar!", bd=3, bg='#187db2', font=('roboto', 12, 'bold italic'), command=self.verificarDisponibilidade)
        self.btnAnalizarF1.place(x=175, y=70, width=120, height=40)
        #objetos do Frame1_1
        self.label2F1 = Label(self.frame1_1, text="Ruas Disponiveis: ", font=('verdana', 11, 'bold'), bg='#dfe3ee', fg='#187db2')
        self.label2F1.place(x= 165, y= 20, width=150, height=20)
        self.rRuasDisponiveisRetorno = Label(self.frame1_1, textvariable=rRuasDisponiveis, anchor='w', font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='black')
        self.rRuasDisponiveisRetorno.place(x=5, y=65, width=460, height= 20)
        self.rRuasDisponiveisRetorno2 = Label(self.frame1_1, textvariable=rRuasDisponiveis2, anchor='w', font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='black')
        self.rRuasDisponiveisRetorno2.place(x=5, y=85, width=460, height= 20)
        self.rRuasDisponiveisRetorno3 = Label(self.frame1_1, textvariable=rRuasDisponiveis3, anchor='w', font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='black')
        self.rRuasDisponiveisRetorno3.place(x=5, y=105, width=460, height= 20)
        #Objetos do Frame2
        self.btnBloqF2 = Button(self.frame2, text="Consultar Bloqueados", bd=3, bg='#187db2', font=('roboto', 10, 'bold italic'))
        self.btnBloqF2.place(x=160, y=125, width=150, height=40)
        #Objetos do Frame3
        self.label1F3 = Label(self.frame3, text="O que deseja consultar?", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label1F3.place(x=145, y=7, width=180, height=20)
        self.edadoF3 = ttk.Combobox(self.frame3, values=["Item", "Rua"])
        self.edadoF3.place(x=145, y=32, width=180, height=20)
        self.label2F3 = Label(self.frame3, text="Digite o número:", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label2F3.place(x=145, y=57, width=180, height=20)
        self.enumeroF3 = Entry(self.frame3, bd=2, validate="key", validatecommand=self.verificaEnumeroF3)
        self.enumeroF3.place(x=145, y=82, width=180, height=20)
        self.btnConsultarF3 = Button(self.frame3, text="Realizar Consulta!",bd=3, bg='#187db2', font=('roboto', 12, 'bold italic'), command=self.realizarConsulta)
        self.btnConsultarF3.place(x=145, y=107, width=180, height=30)
        #Objetos do Frame3_1
        self.label3F3 = Label(self.frame3_1, text="Item:", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label3F3.place(x=10, y=10, width=50, height=20)
        self.rConsultaF3 = Label(self.frame3_1, textvariable=rConsultaNumero, anchor='w', font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='black')
        self.rConsultaF3.place(x=120, y=10, width=100, height=20)
        self.label4F3 = Label(self.frame3_1, text="Descrição:", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label4F3.place(x=10, y=30, width=100, height=20)
        self.rConsulta2F3 = Label(self.frame3_1, textvariable=rConsultaDescricao, anchor='w', font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='black')
        self.rConsulta2F3.place(x=120, y=30, width=300, height=20)
        self.label5F3 = Label(self.frame3_1, text="Peso:", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label5F3.place(x=10, y=50, width=50, height=20)
        self.rConsulta3F3 = Label(self.frame3_1, textvariable=rConsultaPeso, anchor='w', font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='black')
        self.rConsulta3F3.place(x=120, y=50, width=80, height=20)
        self.label6F3 = Label(self.frame3_1, text="Altura:", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label6F3.place(x=10, y=70, width=80, height=20)
        self.rConsulta4F3 = Label(self.frame3_1, textvariable=rConsultaAltura, anchor='w', font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='black')
        self.rConsulta4F3.place(x=120, y=70, width=80, height=20)
        self.label7F3 = Label(self.frame3_1, text="Largura:", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label7F3.place(x=10, y=90, width=80, height=20)
        self.rConsulta5F3 = Label(self.frame3_1, textvariable=rConsultaLargura, anchor='w', font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='black')
        self.rConsulta5F3.place(x=120, y=90, width=80, height=20)
        self.label8F3 = Label(self.frame3_1, text="Comprimento:", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label8F3.place(x=10, y=110, width=100, height=20)
        self.rConsulta6F3 = Label(self.frame3_1, textvariable=rConsultaComprimento, anchor='w', font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='black')
        self.rConsulta6F3.place(x=120, y=110, width=80, height=20)
        #Objetos do Frame3_2
        self.label9F3 = Label(self.frame3_2, text="Rua:", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label9F3.place(x=10, y=20, width=150, height=20)
        self.rConsulta7F3 = Label(self.frame3_2, textvariable=rConsultaNumero, anchor='w', font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='black')
        self.rConsulta7F3.place(x=180, y=20, width=100, height=20)
        self.label10F3 = Label(self.frame3_2, text="Peso Máximo:", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label10F3.place(x=10, y=40, width=150, height=20)
        self.rConsulta8F3 = Label(self.frame3_2, textvariable=rConsultaPeso, anchor='w', font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='black')
        self.rConsulta8F3.place(x=180, y=40, width=80, height=20)
        self.label11F3 = Label(self.frame3_2, text="Altura Máxima:", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label11F3.place(x=10, y=60, width=150, height=20)
        self.rConsulta9F3 = Label(self.frame3_2, textvariable=rConsultaAltura, anchor='w', font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='black')
        self.rConsulta9F3.place(x=180, y=60, width=80, height=20)
        self.label12F3 = Label(self.frame3_2, text="Largura Máxima:", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label12F3.place(x=10, y=80, width=150, height=20)
        self.rConsulta10F3 = Label(self.frame3_2, textvariable=rConsultaLargura, anchor='w', font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='black')
        self.rConsulta10F3.place(x=180, y=80, width=80, height=20)
        self.label13F3 = Label(self.frame3_2, text="Comprimento Máximo:", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label13F3.place(x=10, y=100, width=150, height=20)
        self.rConsulta11F3 = Label(self.frame3_2, textvariable=rConsultaComprimento, anchor='w', font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='black')
        self.rConsulta11F3.place(x=180, y=100, width=80, height=20)
        #Objetos do Frame4
        self.label1F4 = Label(self.frame4, text="Item do Material", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2')
        self.label1F4.place(x=180, y=50, width=120, height=15)
        self.vitemF4 = Entry(self.frame4, bd=2, validate="key", validatecommand=self.verificaVitemF4)
        self.vitemF4.place(x=180, y=70, width=120, height=20)
        self.label2F4 = Label(self.frame4, text="Descrição", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2')
        self.label2F4.place(x=110, y=95, width=260, height=15)
        self.vdescricaoF4 = Entry(self.frame4, bd=2)
        self.vdescricaoF4.place(x=110, y=115, width=260, height=20)
        self.label3F4 = Label(self.frame4, text="Peso", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2')
        self.label3F4.place(x=110, y=140, width=120, height=15)
        self.vpesoF4 = Entry(self.frame4, bd=2, validate="key", validatecommand=self.verificaVpesoF4)
        self.vpesoF4.place(x=110, y=160, width=120, height=20)
        self.label4F4 = Label(self.frame4, text="Altura", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2')
        self.label4F4.place(x=250, y=140, width=120, height=15)
        self.valturaF4 = Entry(self.frame4, bd=2, validate="key", validatecommand=self.verificaValturaF4)
        self.valturaF4.place(x=250, y=160, width=120, height=20)
        self.label5F4 = Label(self.frame4, text="Largura", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2')
        self.label5F4.place(x=110, y=185, width=120, height=15)
        self.vlarguraF4 = Entry(self.frame4, bd=2, validate="key", validatecommand=self.verificaVlarguraF4)
        self.vlarguraF4.place(x=110, y=205, width=120, height=20)
        self.label6F4 = Label(self.frame4, text="Comprimento", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2')
        self.label6F4.place(x=250, y=185, width=120, height=15)
        self.vcomprimentoF4 = Entry(self.frame4, bd=2, validate="key", validatecommand=self.verificaVcomprimentoF4)
        self.vcomprimentoF4.place(x=250, y=205, width=120, height=20)
        self.btnCriarItemF4 = Button(self.frame4, text="Criar Item", bd=3, bg='#187db2', font=('roboto', 12, 'bold italic'), command=self.criarItem)
        self.btnCriarItemF4.place(x=180, y=240, width=120, height=30)
        #Objetos do Frame5
        self.label1F5 = Label(self.frame5, text="Digite o item que deseja editar", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label1F5.place(x=115, y=60, width=250, height=15)
        self.eitemF5 = Entry(self.frame5, bd=2, validate="key", validatecommand=self.verificaEitemF5)
        self.eitemF5.place(x=115, y=80, width=250, height=20)
        self.label2F5 = Label(self.frame5, text="Escolha qual o dado será editado", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label2F5.place(x=115, y=110, width=250, height=15)
        self.edadoF5 = ttk.Combobox(self.frame5, values=["Descrição", "Peso", "Altura", "Largura", "Comprimento"])
        self.edadoF5.place(x=115, y=130, width=250, height=20)
        self.label3F5 = Label(self.frame5, text="Digite o novo valor para o dado", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label3F5.place(x=115, y=160, width=250, height=15)
        self.novoDadoF5 = Entry(self.frame5, bd=2)
        self.novoDadoF5.place(x=115, y=180, width=250, height=20)
        self.btnEditarItemF5 = Button(self.frame5, text="Salvar Alteração!", bd=3, bg='#187db2', font=('roboto', 12, 'bold italic'), command=self.editarItens)
        self.btnEditarItemF5.place(x=115, y=215, width=250, height=30)
        #Objetos do Frame6
        self.label1F6 = Label(self.frame6, text="Endereço da Rua", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2')
        self.label1F6.place(x=160, y=60, width=150, height=15)
        self.vruaF6 = Entry(self.frame6, bd=2, validate="key", validatecommand=self.verificaVruaF6)
        self.vruaF6.place(x=160, y=80, width=150, height=20)
        self.label2F6 = Label(self.frame6, text="Peso Máximo", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2')
        self.label2F6.place(x=75, y=110, width=150, height=15)
        self.vpesoMaximoF6 = Entry(self.frame6, bd=2, validate="key", validatecommand=self.verificaVpesoMaximoF6)
        self.vpesoMaximoF6.place(x=75, y=130, width=150, height=20)
        self.label3F6 = Label(self.frame6, text="Altura Máxima", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2')
        self.label3F6.place(x=245, y=110, width=150, height=15)
        self.valturaMaximaF6 = Entry(self.frame6, bd=2, validate="key", validatecommand=self.verificaValturaMaximaF6)
        self.valturaMaximaF6.place(x=245, y=130, width=150, height=20)
        self.label4F6 = Label(self.frame6, text="Largura Máxima", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2')
        self.label4F6.place(x=75, y=160, width=150, height=15)
        self.vlarguraMaximaF6 = Entry(self.frame6, bd=2, validate="key", validatecommand=self.verificaVlarguraMaximaF6)
        self.vlarguraMaximaF6.place(x=75, y=180, width=150, height=20)
        self.label5F6 = Label(self.frame6, text="Comprimento Máximo", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2')
        self.label5F6.place(x=245, y=160, width=150, height=15)
        self.vcomprimentoMaximoF6 = Entry(self.frame6, bd=2, validate="key", validatecommand=self.verificaVcomprimentoMaximoF6)
        self.vcomprimentoMaximoF6.place(x=245, y=180, width=150, height=20)
        self.btnCriarRuaF6 = Button(self.frame6, text="Criar Rua", bd=3, bg='#187db2', font=('roboto', 12, 'bold italic'), command=self.criarRua)
        self.btnCriarRuaF6.place(x=160, y=225, width=150, height=30)
        #Objetos do Frame7
        self.label1F7 = Label(self.frame7, text="Digite a rua que deseja editar", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label1F7.place(x=115, y=60, width=250, height=15)
        self.eruaF7 = Entry(self.frame7, bd=2, validate="key", validatecommand=self.verificaEruaF7)
        self.eruaF7.place(x=115, y=80, width=250, height=20)
        self.label2F7 = Label(self.frame7, text="Escolha qual o dado será editado", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label2F7.place(x=115, y=110, width=250, height=15)
        self.edadoF7 = ttk.Combobox(self.frame7, values=["Peso Máximo", "Altura Máxima", "Largura Máxima", "Comprimento Máximo"])
        self.edadoF7.place(x=115, y=130, width=250, height=20)
        self.label3F7 = Label(self.frame7, text="Digite o novo valor para o dado", font=('verdana', 9, 'bold'), bg='#dfe3ee', fg='#187db2', anchor='w')
        self.label3F7.place(x=115, y=160, width=250, height=15)
        self.novoDadoF7 = Entry(self.frame7, bd=2, validate="key", validatecommand=self.verificaNovoDadoF7)
        self.novoDadoF7.place(x=115, y=180, width=250, height=20)
        self.btnEditarRuaF7 = Button(self.frame7, text="Salvar Alteração!", bd=3, bg='#187db2', font=('roboto', 12, 'bold italic'), command=self.editarRuas)
        self.btnEditarRuaF7.place(x=115, y=215, width=250, height=30)
    def validaEntradas(self): 
        self.verificaVitemF1 = (self.janela.register(self.validadorOitoDigitosNumericos), "%P")
        self.verificaEnumeroF3 = (self.janela.register(self.validadorOitoDigitosNumericos), "%P")
        self.verificaVitemF4 = (self.janela.register(self.validadorOitoDigitosNumericos), "%P")
        self.verificaVpesoF4 = (self.janela.register(self.validadorQuatroDigitosNumericos), "%P")
        self.verificaValturaF4 = (self.janela.register(self.validadorQuatroDigitosNumericos), "%P")
        self.verificaVlarguraF4 = (self.janela.register(self.validadorQuatroDigitosNumericos), "%P")
        self.verificaVcomprimentoF4 = (self.janela.register(self.validadorQuatroDigitosNumericos), "%P")
        self.verificaEitemF5 = (self.janela.register(self.validadorOitoDigitosNumericos), "%P")
        self.verificaVruaF6 = (self.janela.register(self.validadorDoisDigitosNumericos), "%P")
        self.verificaVpesoMaximoF6 = (self.janela.register(self.validadorQuatroDigitosNumericos), "%P")
        self.verificaValturaMaximaF6 = (self.janela.register(self.validadorQuatroDigitosNumericos), "%P")
        self.verificaVlarguraMaximaF6 = (self.janela.register(self.validadorQuatroDigitosNumericos), "%P")
        self.verificaVcomprimentoMaximoF6 = (self.janela.register(self.validadorQuatroDigitosNumericos), "%P")
        self.verificaEruaF7 = (self.janela.register(self.validadorDoisDigitosNumericos), "%P")
        self.verificaNovoDadoF7 = (self.janela.register(self.validadorQuatroDigitosNumericos), "%P")
Aplicacao()