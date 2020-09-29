# ValidArgsTester

Um sistema para provar se um argumento é válido.
Desenvolvido para Disciplina de Inteligência Artificial


# Como funciona?

Aplicando regras de inferências, que são argumentos válidos conhecidos.
As inferências são obtidas da entrada padrão (stdin).

# Operadores


Operador | Símbolo
-----------|-----------
SE         | ->
OU         | .
NAO        | '
PROVAR     | @


# Regras de inferência implementadas
+	Modus Pones
+	Modus Tolens
+	Silogismo Hipotético

# Siglas

Sigla      | Significado
-----------|-----------
CQD        | Como Queira Demonstrar
MP         | Modus Pones
SH         | Silogismo Hipotético
MT         | Modus Tolens
.:.        | Portanto 

# Exemplo

<pre><font color="#8AE234"><b>danny@hakurei</b></font>:<font color="#729FCF"><b>~/Dev/ValidArgsTester</b></font>$ ./trabalho2.py 
Digite cada uma das proposições
Por último digite o argumento a ser provado!
E este deve ser iniciado com @, exemplo: @ (s)&apos;
proposicao: 
t -&gt; q
proposicao: 
(q)&apos;
proposicao: 
@ (t)&apos;
proposicao: 

MT (0 , 1) 	t -&gt; q, (q)&apos;
	____________________
.:.		(t)&apos;
[&quot;(t)&apos;&quot;]


cqd: [&quot;(t)&apos;&quot;]
<font color="#8AE234"><b>danny@hakurei</b></font>:<font color="#729FCF"><b>~</b></font></pre>

