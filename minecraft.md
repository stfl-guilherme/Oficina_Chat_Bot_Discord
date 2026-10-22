# Guia de Referência do Minecraft Vanilla (Java e Bedrock)

Documento de referência para uso com RAG. Cada seção que começa com "##" é autocontida e pode ser lida sozinha. Marcações usadas: **[Java]** vale só para a Java Edition, **[Bedrock]** vale só para a Bedrock Edition, **[Ambas]** vale para as duas. Nomes de itens e mobs aparecem em português com o nome em inglês entre parênteses, porque jogadores costumam usar os dois.

Atualizado em outubro de 2026. Cobre o jogo até a Java Edition 26.3 (Wilderness Bound, lançada em 15 de setembro de 2026) e a versão equivalente da Bedrock. Conteúdo de snapshots e previews (versões de teste) está marcado como "em teste" e pode mudar.

---

# PARTE 1 — FUNDAMENTOS

## Edições do Minecraft: Java e Bedrock

O Minecraft tem duas edições principais. A **Java Edition** roda em computadores (Windows, macOS e Linux), aceita mods com facilidade e é a edição usada pela maioria dos servidores técnicos e de minigames de PC. A **Bedrock Edition** roda em Windows, consoles (Xbox, PlayStation, Nintendo Switch), celulares (Android e iOS) e permite multiplayer entre todas essas plataformas (crossplay). Na Bedrock existe o Marketplace, uma loja oficial de mapas, skins e add-ons.

No PC, quem compra o jogo recebe as duas edições juntas ("Minecraft: Java & Bedrock Edition for PC"). As duas edições têm quase o mesmo conteúdo, mas mecânicas diferentes em combate, redstone, geração de mobs e alguns detalhes. As diferenças estão marcadas ao longo do documento e resumidas na Parte 6.

"Vanilla" significa o jogo original, sem mods nem plugins.

## Versões atuais e a nova numeração (26.x)

Desde 2026 a Mojang usa numeração por ano no formato ANO.DROP.HOTFIX. Por isso não existe "Minecraft 1.22": depois da 1.21.11 (dezembro de 2025) veio a 26.1. Exemplo: 26.3 é o terceiro "game drop" de 2026; 26.3.1 seria um hotfix dele. A Bedrock tem sua própria numeração (por exemplo, o drop 26.2 da Java saiu como Bedrock 26.30).

Os "game drops" são atualizações menores lançadas cerca de quatro vezes por ano, no lugar da antiga grande atualização anual.

Drops de 2026 lançados:
- **26.1 — Tiny Takeover** (março de 2026): filhotes de mobs redesenhados, Dente-de-leão Dourado, etiquetas de nome craftáveis.
- **26.2 — Chaos Cubed** (16 de junho de 2026): bioma Cavernas de Enxofre, mob Cubo de Enxofre, gêiseres, lista de amigos na Java, renderizador Vulkan experimental na Java.
- **26.3 — Wilderness Bound** (15 de setembro de 2026): bioma Floresta Matizada (Dappled Forest), árvores de Choupo (Poplar), Acampamentos Abandonados, almofadas, cama de palha, escadas e lajes de lã e de concreto.

Em teste em outubro de 2026: o drop de inverno (26.4), com Cavernas de Gelo e um novo zumbi chamado Frostbite. Ainda não foi lançado.

**[Java]** A partir da 26.1, rodar um servidor Java exige o Java 25. Jogadores comuns não precisam se preocupar, porque o launcher oficial já traz o Java certo.

## Modos de jogo

**[Ambas]**
- **Sobrevivência (Survival):** você coleta recursos, tem vida e fome e pode morrer. É o modo principal.
- **Criativo (Creative):** recursos infinitos, voo, sem dano. Para construir livremente.
- **Aventura (Adventure):** para mapas feitos por outros jogadores; só é possível quebrar ou colocar blocos permitidos pelo criador do mapa.
- **Espectador (Spectator):** voa atravessando blocos, invisível, sem interagir com o mundo.
- **Hardcore:** Sobrevivência na dificuldade Difícil travada e com uma única vida. Se morrer, o mundo acaba (vira modo Espectador).

## Dificuldades

**[Ambas]** Pacífico (Peaceful), Fácil (Easy), Normal e Difícil (Hard).
- **Pacífico:** monstros hostis não aparecem, a vida e a fome se recuperam sozinhas.
- **Fácil:** monstros causam menos dano; a fome sozinha deixa você com no mínimo 5 corações.
- **Normal:** a fome sozinha deixa você com no mínimo meio coração.
- **Difícil:** monstros causam mais dano, zumbis podem quebrar portas, e a fome pode matar.

## Interface: vida, fome, armadura e experiência

**[Ambas]**
- **Vida:** 10 corações (20 pontos). Recupera sozinha quando a barra de fome está quase cheia.
- **Fome:** 10 coxinhas (20 pontos). Correr, pular, nadar e lutar gastam fome. Abaixo de 3 coxinhas você não consegue correr. Com a fome zerada você perde vida.
- **Saturação:** valor oculto que funciona como uma reserva antes de a barra de fome começar a cair. Comidas boas dão muita saturação.
- **Armadura:** barra de "peitorais" acima da vida, até 20 pontos.
- **Experiência (XP):** a barra verde. Os níveis servem para encantar e para usar a bigorna. Você ganha XP matando mobs, minerando alguns minérios, usando a fornalha, procriando animais, pescando e negociando com aldeões.
- **Oxigênio:** bolhas que aparecem embaixo d'água. Quando acabam, você começa a perder vida.

## Controles básicos (PC)

**[Java]** W A S D andam; Espaço pula; Shift agacha (você não cai de beiradas agachado); Ctrl ou W duas vezes corre; E abre o inventário; Q solta o item; F troca o item entre a mão principal e a mão secundária; F3 abre a tela de depuração com coordenadas, bioma e direção; F5 muda a câmera; T abre o chat; / abre o chat já com comando. Botão esquerdo do mouse quebra blocos e ataca; botão direito usa itens e coloca blocos.

**[Bedrock]** No PC os controles são parecidos. A coordenada aparece ativando "Mostrar coordenadas" nas configurações do mundo. A mão secundária só aceita alguns itens (escudo, totem, flechas, mapa, foguetes, concha de náutilo, entre outros). No celular os controles são por toque; no console, por controle.

## Ciclo de dia e noite

**[Ambas]** Um dia completo dura 20 minutos reais: cerca de 10 minutos de dia, 1,5 minuto de pôr do sol, 7 minutos de noite e 1,5 minuto de nascer do sol. Dormir em uma cama à noite (ou durante tempestades) pula para a manhã. Em multiplayer, normalmente todos os jogadores precisam dormir; na Java a porcentagem necessária é ajustável pela regra `playersSleepingPercentage`.

## Luz e aparecimento (spawn) de monstros

**[Ambas]** A maioria dos monstros hostis do Overworld (zumbis, esqueletos, creepers, aranhas) aparece apenas onde a luz vinda de blocos é 0. Isso significa que qualquer tocha, lanterna ou outra fonte de luz impede o spawn naquele local. Uma tocha tem luz 14 e ilumina vários blocos ao redor. A luz do sol e da lua também conta: monstros aparecem na superfície à noite e em cavernas escuras a qualquer hora.

Para proteger uma base: ilumine todo o chão por dentro e ao redor dela. Slimes, mobs do Nether e alguns casos especiais seguem regras próprias.

## Coordenadas e altura do mundo

**[Ambas]** O mundo usa três coordenadas: X (leste/oeste), Y (altura) e Z (norte/sul). No Overworld, a altura vai de Y -64 (camada de bedrock, a rocha indestrutível) até Y 320 (limite de construção). O nível do mar é Y 63. Abaixo de Y 0 a pedra vira ardósia profunda (deepslate), que demora mais para minerar.

Ver coordenadas: **[Java]** tecla F3. **[Bedrock]** ativar "Mostrar coordenadas" nas configurações do mundo.

---

# PARTE 2 — GUIA PRÁTICO: DO PRIMEIRO DIA AO FIM DO JOGO

## Primeiro dia passo a passo

1. **Madeira:** segure o botão de quebrar em um tronco de árvore para pegar madeira com a mão. Pegue de 10 a 20 troncos.
2. **Tábuas:** no inventário, 1 tronco vira 4 tábuas (planks).
3. **Mesa de trabalho (Crafting Table):** 4 tábuas em quadrado. Ela libera a grade de crafting 3x3.
4. **Gravetos (Sticks):** 2 tábuas, uma em cima da outra, dão 4 gravetos.
5. **Picareta de madeira:** 3 tábuas em cima e 2 gravetos no meio, para baixo.
6. **Pedra:** minere pedra para conseguir pedregulho (cobblestone) e faça picareta, machado, espada e pá de pedra.
7. **Fornalha (Furnace):** 8 pedregulhos em anel.
8. **Carvão:** minere carvão em paredes de pedra ou faça carvão vegetal (charcoal) queimando troncos na fornalha.
9. **Tochas:** 1 carvão em cima de 1 graveto dá 4 tochas.
10. **Comida:** mate vacas, porcos, galinhas ou ovelhas e asse a carne na fornalha.
11. **Cama:** 3 lãs (de ovelhas) em cima de 3 tábuas. Dormir pula a noite e define seu ponto de renascimento.

Se a noite chegar antes de terminar, cave um buraco em um morro, feche a entrada com blocos e coloque uma tocha dentro.

## Abrigo e primeira noite

**[Ambas]** O abrigo mais rápido é cavar 3 blocos para dentro de uma encosta e fechar a entrada. Coloque tocha dentro para monstros não aparecerem. Uma porta impede a entrada de quase todos os mobs, mas zumbis podem quebrar portas de madeira na dificuldade Difícil.

Cuidados na primeira noite:
- **Creeper:** monstro verde que se aproxima em silêncio e explode. Ataque e recue, ou mantenha distância.
- **Esqueleto (Skeleton):** atira flechas de longe; use cobertura.
- **Aranha (Spider):** escala paredes; só é hostil no escuro.
- **Enderman:** não olhe nos olhos dele. Se ele ficar bravo, fique embaixo de um teto de 2 blocos de altura (ele tem 3 blocos de altura) ou entre na água, que machuca o Enderman.
- **Phantom (Fantasma):** aparece no céu se você ficar 3 noites ou mais sem dormir. Dormir resolve.

## Comida e fome

**[Ambas]** Comidas boas para começar:
- **Bife assado (Steak) e Costeleta de porco assada:** recuperam 4 coxinhas cada e têm ótima saturação. Melhores comidas comuns do jogo.
- **Pão (Bread):** 3 trigos em linha. Fácil de fazer com uma fazenda.
- **Cenoura dourada (Golden Carrot):** 1 cenoura cercada por 8 pepitas de ouro. A melhor saturação entre as comidas comuns; ótima para o meio e o fim do jogo.
- **Batata assada, frango assado, peixe assado e carneiro assado:** boas opções.
- **Maçã dourada (Golden Apple):** 1 maçã cercada por 8 barras de ouro. Dá Absorção (corações extras) e Regeneração. Essencial para lutas difíceis.
- **Maçã dourada encantada:** não pode ser craftada; só aparece em baús de estruturas. Muito mais forte.

Evite: carne podre (rotten flesh) causa o efeito Fome; olho de aranha envenena; frango cru pode causar Fome.

Comer de barriga cheia não é possível, exceto maçãs douradas, garrafa de mel, leite e alguns itens especiais. O leite remove todos os efeitos de status.

## Ferramentas e níveis de material

**[Ambas]** Ordem dos materiais, do mais fraco para o mais forte: madeira, pedra, cobre, ferro, diamante e netherite. O ouro é muito rápido, mas quebra muito rápido também, e tem o mesmo nível de mineração da madeira.

O que cada picareta consegue minerar:
- **Madeira ou ouro:** pedra, carvão.
- **Pedra ou cobre:** também ferro, cobre e lápis-lazúli.
- **Ferro:** também ouro, redstone, diamante e esmeralda.
- **Diamante:** também obsidiana, obsidiana chorona (crying obsidian) e detrito ancestral (ancient debris).
- **Netherite:** o mesmo que diamante, porém mais rápido e mais durável.

Ferramentas: picareta (pedra e minérios), machado (madeira; também é uma arma forte), pá (terra, areia, cascalho, neve), enxada (arar terra; quebra folhas e blocos de feno rápido) e tesoura (lã, folhas, teias).

As ferramentas e armaduras de cobre foram adicionadas no drop The Copper Age (2025), ficando entre pedra e ferro.

## Armadura

**[Ambas]** Peças: capacete, peitoral, calças e botas. Materiais do mais fraco para o mais forte: couro, cobre, ouro, cota de malha, ferro, diamante e netherite. O couro pode ser tingido. A armadura de cota de malha não é craftável: vem de baús, de mobs ou de aldeões armeiros.

- **Armadura completa de ferro:** 15 pontos de armadura.
- **Armadura completa de diamante:** 20 pontos de armadura, mais Resistência (toughness), que ajuda contra golpes fortes.
- **Netherite:** igual ao diamante em pontos, com mais Resistência, resistência a empurrão (knockback) e não queima na lava como item.

Itens especiais de cabeça: casco de tartaruga (respirar debaixo d'água por mais tempo), abóbora entalhada (Endermen não ficam bravos quando você olha para eles) e cabeças de mobs.

Para não ser atacado por piglins no Nether, use pelo menos uma peça de armadura de ouro.

## Fornalha, alto-forno e defumador

**[Ambas]**
- **Fornalha (Furnace):** 8 pedregulhos. Derrete minérios, cozinha comida, faz vidro (com areia), pedra lisa, tijolos e carvão vegetal.
- **Alto-forno (Blast Furnace):** 5 barras de ferro, 1 fornalha e 3 pedras lisas. Derrete minérios e armaduras com o dobro da velocidade, mas não cozinha comida.
- **Defumador (Smoker):** 1 fornalha cercada por 4 troncos. Cozinha comida com o dobro da velocidade.

Combustíveis e quantos itens cada um derrete na fornalha comum:
- Carvão ou carvão vegetal: 8 itens.
- Bloco de carvão: 80 itens.
- Balde de lava: 100 itens (o balde volta vazio).
- Vara de Blaze: 12 itens.
- Bloco de alga seca (dried kelp block): 20 itens.
- Tábua de madeira: 1,5 item.

A fornalha guarda a experiência dos itens derretidos; você recebe o XP ao retirar o resultado.

## Estratégias de mineração

**[Ambas]**
- **Mineração em galerias (branch mining):** desça até a altura do minério desejado e cave um túnel principal com túneis laterais a cada 2 ou 3 blocos. É seguro e eficiente para diamantes.
- **Exploração de cavernas (caving):** cavernas grandes expõem muitos minérios nas paredes, mas são mais perigosas. Leve muitas tochas, comida, um balde de água e blocos para fazer pontes.
- **Nunca cave reto para baixo:** você pode cair em lava ou em uma caverna profunda.
- **Nunca cave reto para cima** debaixo de cascalho ou areia: eles caem e podem sufocar você.
- **Lava:** um balde de água transforma lava parada (fonte) em obsidiana e lava corrente em pedra ou pedregulho.

Kit recomendado: 2 picaretas de ferro, um stack de tochas, comida, balde de água, escudo, blocos de pedra e uma cama.

## Alturas dos minérios (geração atual)

**[Ambas]** Geração de minérios desde a atualização 1.18 (válida também nas versões 26.x). "Pico" é a altura onde o minério é mais comum.

- **Carvão (Coal):** de Y 0 até Y 320; pico perto de Y 95, muito comum em montanhas.
- **Cobre (Copper):** de Y -16 até Y 112; pico perto de Y 48; muito abundante em cavernas de espeleotemas (dripstone caves).
- **Ferro (Iron):** de Y -64 até Y 320; pico perto de Y 16 e muito comum também no alto de montanhas (perto de Y 232).
- **Lápis-lazúli (Lapis Lazuli):** de Y -64 até Y 64; pico perto de Y 0.
- **Ouro (Gold):** de Y -64 até Y 32; pico perto de Y -16. Nas Terras Áridas (Badlands) aparece muito mais, inclusive na superfície.
- **Redstone:** de Y -64 até Y 15; fica mais comum quanto mais fundo.
- **Diamante (Diamond):** de Y -64 até Y 16; fica mais comum quanto mais fundo. A melhor altura é perto de **Y -59** (logo acima da bedrock).
- **Esmeralda (Emerald):** só em biomas de montanha; mais comum no alto das montanhas.
- **Detrito ancestral (Ancient Debris):** só no Nether, de Y 8 até Y 119; mais comum perto de Y 15.
- **Quartzo do Nether e Ouro do Nether:** comuns em todo o Nether.

## Como encontrar diamantes

**[Ambas]** Diamantes ficam entre Y 16 e Y -64 e são mais comuns quanto mais fundo. A melhor altura para procurar é perto de **Y -59**. Passos:

1. Tenha pelo menos uma picareta de ferro (picaretas de pedra ou de cobre não coletam diamante).
2. Desça em escada até Y -59 (veja a altura com F3 na Java ou com "Mostrar coordenadas" na Bedrock).
3. Faça mineração em galerias: um túnel principal e túneis laterais com 2 blocos de distância entre eles.
4. Diamantes que encostam no ar (paredes de cavernas) aparecem com menos frequência, então cavar túneis próprios funciona melhor que só andar em cavernas.
5. Cuidado com lava, que é comum nessas alturas. Leve um balde de água.

Uma picareta com **Fortuna (Fortune)** III rende em média mais diamantes por minério. Toque de Seda (Silk Touch) coleta o bloco de minério inteiro, sem multiplicar.

Diamantes também aparecem em baús de vilas, templos, naufrágios, câmaras enterradas e cidades ancestrais.

## Agricultura

**[Ambas]**
- Use uma **enxada** em terra ou grama para criar terra arada (farmland).
- Água a até 4 blocos de distância hidrata a terra arada, e as plantações crescem mais rápido.
- Plantações precisam de luz (sol ou tochas) para crescer.
- **Farinha de osso (Bone Meal)** acelera o crescimento. Ela vem de ossos de esqueletos ou da composteira (Composter).
- Pisar ou pular na terra arada pode transformá-la de volta em terra.

Plantações principais:
- **Trigo:** sementes vêm de quebrar grama. Serve para pão, para procriar vacas, ovelhas e cabras, e para fardo de feno.
- **Cenoura e batata:** às vezes caem de zumbis ou aparecem em vilas.
- **Beterraba:** sementes de baús de vilas.
- **Abóbora e melancia:** o caule precisa de um bloco livre ao lado para o fruto crescer.
- **Cana-de-açúcar:** precisa estar em areia ou terra ao lado da água. Serve para papel e açúcar.
- **Bambu, cacto, cacau (em troncos de selva), algas (kelp) e frutas doces (sweet berries).**
- **Verruga do Nether (Nether Wart):** cresce só em areia das almas (soul sand); essencial para poções.

## Criação e procriação de animais

**[Ambas]** Dê a comida certa a dois animais da mesma espécie e eles têm um filhote. Comidas para procriar:

- **Vaca, ovelha, mooshroom e cabra:** trigo.
- **Porco:** cenoura, batata ou beterraba.
- **Galinha:** sementes (trigo, beterraba, melancia, abóbora, flor-tocha e jarro).
- **Cavalo e burro:** maçã dourada ou cenoura dourada.
- **Lobo:** qualquer carne (precisa estar domado).
- **Gato:** bacalhau ou salmão crus.
- **Coelho:** cenoura, cenoura dourada ou dente-de-leão.
- **Lhama:** fardo de feno.
- **Tartaruga:** erva marinha (seagrass).
- **Abelha:** qualquer flor.
- **Raposa:** frutas doces.
- **Panda:** bambu.
- **Axolote:** balde de peixe tropical.
- **Sapo:** bola de slime.
- **Camelo:** cacto.
- **Tatu (Armadillo):** olho de aranha.
- **Farejador (Sniffer):** sementes de flor-tocha.

Filhotes crescem em cerca de 20 minutos. Com o **Dente-de-leão Dourado** (adicionado na 26.1) dá para impedir que um filhote cresça.

## Animais de estimação e montarias

**[Ambas]**
- **Lobo (Wolf):** dome dando ossos. Ele luta ao seu lado e pode usar armadura de lobo (feita com escamas de tatu). Existem várias variantes de lobo conforme o bioma.
- **Gato (Cat):** dome com bacalhau ou salmão cru, com cuidado para não assustá-lo. Afasta creepers e phantoms. Às vezes traz presentes de manhã.
- **Papagaio (Parrot):** dome com sementes. Nunca dê biscoito (cookie): ele morre.
- **Cavalo (Horse):** monte nele várias vezes até ele aceitar você; depois coloque uma sela. Pode usar armadura de cavalo.
- **Burro e mula:** podem carregar um baú.
- **Lhama:** carrega baú e anda em caravana.
- **Camelo:** leva 2 jogadores e dá um impulso de corrida.
- **Porco e Strider:** controlados com cenoura no palito e fungo distorcido no palito.
- **Náutilo (Nautilus):** montaria aquática adicionada no drop Mounts of Mayhem (dezembro de 2025).
- **Ghast Feliz (Happy Ghast):** montaria voadora para até 4 jogadores (veja a seção própria).

## Aldeões e comércio

**[Ambas]** Aldeões vivem em vilas e trocam itens por **esmeraldas**. Cada aldeão tem uma profissão definida pelo bloco de trabalho mais próximo que ele tomar para si. Fazendo negócios, o aldeão sobe de nível (Novato, Aprendiz, Experiente, Especialista e Mestre) e libera trocas melhores.

Dicas:
- Um aldeão sem trocas feitas pode mudar de profissão se você quebrar e recolocar o bloco de trabalho. Assim dá para "rolar" bibliotecários até sair um livro bom, como Remendo (Mending).
- **Curar um aldeão zumbi** dá grandes descontos permanentes: arremesse uma poção de Fraqueza (splash) nele e depois dê uma maçã dourada.
- **Aldeões procriam** quando há camas livres e eles têm comida suficiente (pão, cenoura, batata ou beterraba).
- O **Golem de Ferro** protege a vila.
- O **Mercador Ambulante (Wandering Trader)** aparece de vez em quando e vende itens raros de outros biomas.

## Profissões e blocos de trabalho

**[Ambas]**
- **Armeiro (Armorer):** Alto-forno. Vende armaduras.
- **Açougueiro (Butcher):** Defumador.
- **Cartógrafo (Cartographer):** Mesa de cartografia. Vende mapas de exploração.
- **Clérigo (Cleric):** Suporte de poções. Vende pérolas do Ender, redstone, lápis.
- **Fazendeiro (Farmer):** Composteira. Compra plantações (ótimo para conseguir esmeraldas).
- **Pescador (Fisherman):** Barril.
- **Flecheiro (Fletcher):** Mesa de arco e flecha. Compra gravetos (outra fonte fácil de esmeraldas).
- **Coureiro (Leatherworker):** Caldeirão.
- **Bibliotecário (Librarian):** Púlpito (Lectern). Vende livros encantados, inclusive Remendo.
- **Pedreiro (Mason):** Cortador de pedras.
- **Pastor (Shepherd):** Tear.
- **Ferramenteiro (Toolsmith):** Mesa de ferraria.
- **Ferreiro de armas (Weaponsmith):** Rebolo (Grindstone).

Aldeões sem profissão ficam desempregados; aldeões bobos (nitwit), de roupa verde, nunca trabalham.

## Mesa de encantamentos

**[Ambas]** Receita: 1 livro, 2 diamantes e 4 obsidianas. Para encantar, coloque o item e lápis-lazúli; você escolhe entre 3 opções e gasta níveis de XP.

Para liberar o encantamento de nível 30 (o máximo da mesa), coloque **15 estantes de livros (bookshelves)** ao redor da mesa, com exatamente 1 bloco de ar entre a mesa e as estantes, na mesma altura ou um bloco acima. Uma estante = 6 tábuas e 3 livros.

Alguns encantamentos nunca saem da mesa e só são obtidos com aldeões, baús ou pesca: Remendo (Mending), Pés Ágeis da Alma (Soul Speed), Passos Furtivos (Swift Sneak), Passos Gelados (Frost Walker) e as Maldições.

## Encantamentos mais importantes

**[Ambas]** Nível máximo entre parênteses.

Ferramentas:
- **Eficiência (Efficiency) V:** mineração mais rápida.
- **Inquebrável (Unbreaking) III:** dura mais.
- **Fortuna (Fortune) III:** mais drops de minérios como diamante, carvão, lápis, redstone e esmeralda. Não combina com Toque de Seda.
- **Toque de Seda (Silk Touch) I:** coleta o bloco original (minério inteiro, vidro, gelo, ninho de abelha).
- **Remendo (Mending) I:** o XP que você coleta conserta o item. O encantamento mais valioso do jogo.

Armas:
- **Afiação (Sharpness) V:** mais dano em tudo. Não combina com Julgamento nem Ruína dos Artrópodes.
- **Julgamento (Smite) V:** dano extra contra mortos-vivos (zumbis, esqueletos, Wither).
- **Saque (Looting) III:** mais drops de mobs.
- **Aspecto Flamejante (Fire Aspect) II** e **Repulsão (Knockback) II.**
- **Golpe de Varredura (Sweeping Edge) III:** **[Java]** apenas.

Armadura:
- **Proteção (Protection) IV:** reduz quase todos os tipos de dano. Não combina com Proteção contra Fogo, Explosões ou Projéteis.
- **Queda Suave (Feather Falling) IV:** botas; reduz dano de queda.
- **Respiração (Respiration) III** e **Afinidade Aquática (Aqua Affinity) I:** capacete, para água.
- **Passos Profundos (Depth Strider) III:** botas, anda mais rápido na água.
- **Espinhos (Thorns) III:** devolve dano.
- **Passos Furtivos (Swift Sneak) III:** calças; anda agachado mais rápido. Só nas Cidades Ancestrais.

Arcos e bestas: **Força (Power) V**, **Impacto (Punch) II**, **Chama (Flame) I**, **Infinidade (Infinity) I** (flechas infinitas com 1 flecha no inventário; **[Java]** não combina com Remendo), **Disparo Múltiplo (Multishot)**, **Perfuração (Piercing)** e **Recarga Rápida (Quick Charge) III**.

Tridente: **Lealdade (Loyalty) III**, **Correnteza (Riptide) III**, **Condutividade (Channeling) I** e **Empalamento (Impaling) V**.

Maça: **Densidade (Density) V**, **Ruptura (Breach) IV** e **Rajada de Vento (Wind Burst) III**. Lança: **Investida (Lunge)**.

Maldições: **Maldição do Ligamento (Binding)** (a peça não sai do corpo) e **Maldição do Desaparecimento (Vanishing)** (o item some ao morrer).

## Bigorna e rebolo

**[Ambas]**
- **Bigorna (Anvil):** 3 blocos de ferro e 4 barras de ferro. Junta livros encantados com itens, junta dois itens iguais para somar encantamentos e durabilidade, conserta itens com o material deles e renomeia itens. Cada uso deixa o item mais caro de modificar no futuro. **[Java]** Se o custo chegar a 40 níveis, aparece "Caro demais!" (Too Expensive) e a operação fica bloqueada.
- **Rebolo (Grindstone):** remove encantamentos (menos as maldições) e devolve parte do XP. Também conserta juntando dois itens iguais, mas perde os encantamentos.

Dica: aplique primeiro os encantamentos mais caros, e junte livros com livros antes de aplicá-los no item.

## Poções: como começar

**[Ambas]**
1. **Suporte de poções (Brewing Stand):** 1 vara de Blaze e 3 pedregulhos (ou pedra-negra).
2. **Combustível:** pó de Blaze.
3. **Base:** garrafas de vidro com água + **Verruga do Nether** = Poção Estranha (Awkward Potion).
4. **Ingrediente de efeito:** adicionado à Poção Estranha.
5. **Modificadores opcionais:** pó de redstone aumenta a duração; pó de pedra luminosa (glowstone) aumenta a potência (nível II); olho de aranha fermentado corrompe o efeito; pólvora transforma em poção de arremesso (splash); bafo do dragão transforma a de arremesso em persistente (lingering).

A verruga do Nether cresce nas fortalezas do Nether. As varas de Blaze vêm dos Blazes, também nas fortalezas.

## Receitas de poções

**[Ambas]** Todas partem da Poção Estranha, exceto a Fraqueza.
- **Velocidade (Swiftness):** açúcar.
- **Salto (Leaping):** pé de coelho.
- **Cura (Healing):** fatia de melancia reluzente.
- **Veneno (Poison):** olho de aranha.
- **Regeneração:** lágrima de Ghast.
- **Força (Strength):** pó de Blaze.
- **Resistência ao Fogo:** creme de magma. Essencial para o Nether.
- **Visão Noturna:** cenoura dourada.
- **Respiração Aquática:** baiacu.
- **Queda Lenta (Slow Falling):** membrana de Phantom.
- **Mestre Tartaruga (Turtle Master):** casco de tartaruga.
- **Carga de Vento (Wind Charging):** vara de Breeze.
- **Gosma (Oozing):** bloco de slime.
- **Infestação:** pedra.
- **Tecelagem (Weaving):** teia de aranha.

Com olho de aranha fermentado: Cura vira Dano (Harming); Veneno vira Dano; Visão Noturna vira Invisibilidade; Velocidade e Salto viram Lentidão. **Fraqueza (Weakness):** garrafa de água + olho de aranha fermentado (sem verruga).

**[Bedrock]** Existe a Poção da Decomposição (Decay), que causa o efeito Murchar (Wither); ela não pode ser feita no suporte, só obtida com comandos ou no Criativo.

## Como chegar ao Nether

**[Ambas]**
1. Consiga pelo menos **10 obsidianas**. Obsidiana se forma quando água toca uma fonte de lava e só pode ser minerada com picareta de diamante ou netherite. Alternativa: monte a moldura despejando água em lava nos lugares certos, sem minerar.
2. Monte uma moldura retangular de **4 blocos de largura por 5 de altura** (os cantos não são necessários).
3. Acenda com **isqueiro (Flint and Steel)**: 1 barra de ferro + 1 pederneira (flint, que vem de cascalho).
4. Entre no portal roxo e espere alguns segundos.

Portais em ruínas (Ruined Portals) espalhados pelo mundo podem ser completados.

**Escala:** 1 bloco andado no Nether equivale a 8 blocos no Overworld. Por isso o Nether é usado para viajar rápido.

## Sobrevivência no Nether

**[Ambas]**
- **Leve:** armadura com pelo menos 1 peça de ouro (para os piglins), poções de Resistência ao Fogo, muitos blocos, comida, arco, escudo e uma picareta extra.
- **Não durma:** camas explodem no Nether (e no End).
- **Água evapora** quando colocada no Nether.
- **Ghast:** atira bolas de fogo que explodem. Rebata a bola com um golpe ou com flecha. Paredes de pedregulho resistem bem.
- **Piglins:** neutros se você usar ouro. Ficam bravos se você abrir baús ou minerar ouro perto deles.
- **Escambo (Bartering):** jogue barras de ouro para um piglin; ele devolve um item aleatório, como pérolas do Ender, poções de Resistência ao Fogo, obsidiana, linha, couro, quartzo, areia das almas, pedra-negra (blackstone) ou livros de Pés Ágeis da Alma.
- **Strider:** anda sobre a lava. Com sela e fungo distorcido no palito, vira montaria em lagos de lava.
- Anote as coordenadas do portal. Sem isso, é fácil se perder.

## Biomas e estruturas do Nether

**[Ambas]** Biomas:
- **Desertos do Nether (Nether Wastes):** o bioma clássico de netherrack.
- **Floresta Carmesim (Crimson Forest):** hoglins e piglins.
- **Floresta Distorcida (Warped Forest):** a mais segura; cheia de Endermen.
- **Vale de Areia das Almas (Soul Sand Valley):** esqueletos, ghasts e fósseis.
- **Deltas de Basalto (Basalt Deltas):** cubos de magma; terreno difícil.

Estruturas:
- **Fortaleza do Nether (Nether Fortress):** feita de tijolos do Nether. Tem Blazes (varas de Blaze), esqueletos Wither (cabeças para invocar o Wither) e verruga do Nether.
- **Bastião em Ruínas (Bastion Remnant):** feito de pedra-negra, cheio de piglins e piglins brutos. Tem baús com ouro, o **Molde de Melhoria de Netherite** e às vezes detrito ancestral.
- **Portal em Ruínas** e **Fósseis do Nether.**

## Netherite

**[Ambas]**
1. Encontre **detrito ancestral (Ancient Debris)** no Nether, mais comum perto de Y 15. Precisa de picareta de diamante ou netherite. Ele resiste a explosões, então **[Java e Bedrock]** muitos jogadores explodem túneis com camas ou TNT para expor vários de uma vez.
2. Derreta o detrito na fornalha: vira **fragmento de netherite (Netherite Scrap)**.
3. **Barra de netherite:** 4 fragmentos de netherite + 4 barras de ouro.
4. Na **Mesa de Ferraria (Smithing Table)**, combine o **Molde de Melhoria de Netherite**, um item de diamante e uma barra de netherite. O item mantém os encantamentos.

O Molde de Melhoria de Netherite aparece em baús de Bastiões. Para copiar um molde: 1 molde + 7 diamantes + 1 netherrack resultam em 2 moldes.

Itens de netherite flutuam na lava e não queimam.

## Olhos do Ender e a Fortaleza (Stronghold)

**[Ambas]** O portal para o End fica dentro de uma **Fortaleza (Stronghold)** subterrânea no Overworld.

1. **Pérolas do Ender:** caem de Endermen ou vêm de escambo com piglins e de clérigos.
2. **Pó de Blaze:** 1 vara de Blaze dá 2 pós.
3. **Olho do Ender:** 1 pérola do Ender + 1 pó de Blaze.
4. Arremesse um olho do Ender: ele voa na direção da fortaleza mais próxima. Ande nessa direção e jogue de novo. Quando o olho descer, a fortaleza está embaixo. Cada olho tem chance de quebrar ao ser jogado.
5. Cave até a fortaleza e procure a **sala do portal do End**, que tem uma moldura sobre lava e uma cela com Traça (Silverfish) gerando.
6. O portal precisa de 12 olhos do Ender. Alguns já vêm encaixados; você completa o resto.

Leve pelo menos 12 a 15 olhos do Ender. Uma ideia segura é levar de 6 a 8 varas de Blaze.

## O End e o Ender Dragon

**[Ambas]** Antes de entrar no End:
- Armadura de diamante ou netherite encantada, espada e arco encantados, muitas flechas, comida, maçãs douradas, poção de Queda Lenta, blocos (pedregulho), balde de água e uma abóbora entalhada na cabeça (para Endermen não ficarem bravos).

Como lutar:
1. Ao chegar, você está numa ilha cheia de Endermen e pilares de obsidiana.
2. No alto dos pilares há **Cristais do End**, que curam o dragão. Destrua todos com flechas. Alguns estão protegidos por gaiolas de ferro: suba nesses pilares com blocos e quebre o cristal de perto, com cuidado com a explosão.
3. Depois que os cristais acabarem, ataque o dragão. Ele pousa no portal central de vez em quando: é a hora de bater com a espada.
4. Cuidado com o **Bafo do Dragão** (nuvem roxa), que causa dano. Use garrafas vazias na nuvem para coletar Bafo do Dragão para poções persistentes.
5. Técnica avançada: camas explodem no End e causam muito dano no dragão quando ele está pousado, mas também machucam você.

Recompensas: muito XP, o **Ovo do Dragão** (troféu; ele se teletransporta se for clicado, então empurre-o com um pistão ou quebre o bloco embaixo dele e coloque uma tocha), o portal de saída e um **Portal de Passagem do End (End Gateway)**.

O dragão tem 200 pontos de vida (100 corações). Para reinvocá-lo, coloque 4 Cristais do End nas bordas do portal de saída.

## Depois do dragão: Cidades do End, élitros e shulkers

**[Ambas]** O Portal de Passagem aparece flutuando depois de derrotar o dragão. Jogue uma pérola do Ender nele para chegar às ilhas externas do End.

- **Cidades do End (End Cities):** torres roxas com baús cheios de itens encantados de diamante e ferro.
- **Shulkers:** mobs em forma de caixa que atiram projéteis que fazem você levitar. Dropam **cascas de shulker**: 2 cascas + 1 baú = **Caixa de Shulker (Shulker Box)**, um baú portátil que mantém os itens dentro ao ser quebrado.
- **Navio do End (End Ship):** às vezes aparece junto a uma cidade. Tem os **Élitros (Elytra)** na moldura de item e uma cabeça de dragão.
- **Élitros:** asas para planar. Use **foguetes de fogos de artifício** (papel + pólvora) para ganhar impulso no ar. Encante com Remendo e Inquebrável.
- **Frutas do Coro (Chorus Fruit):** teletransportam você para perto; assadas viram fruta do coro estourada.

## O Wither e o Sinalizador (Beacon)

**[Ambas]**
**Invocar o Wither:** coloque 4 blocos de areia das almas (ou solo das almas) em formato de T e 3 cabeças de esqueleto Wither em cima. A última peça colocada tem que ser uma cabeça.
- O Wither é um chefe que voa, atira caveiras explosivas e causa o efeito Murchar (Wither), que tira vida aos poucos.
- Lute em um lugar fechado e longe da sua base; muitos jogadores lutam bem no subterrâneo.
- Use **espada com Julgamento (Smite)**, poções de Cura e Força, leite (remove o efeito Murchar) e maçãs douradas.
- Quando fica com metade da vida, ele ganha um escudo contra flechas.
- **[Bedrock]** O Wither é mais forte: tem mais vida e um ataque de investida.

Recompensa: a **Estrela do Nether (Nether Star)**.

**Sinalizador (Beacon):** 1 Estrela do Nether + 5 vidros + 3 obsidianas. Coloque em cima de uma pirâmide de blocos de ferro, ouro, esmeralda, diamante ou netherite. Níveis da pirâmide: 9 blocos (nível 1), 34 (nível 2), 83 (nível 3) e 164 (nível 4). Ele dá efeitos numa área, como Velocidade, Pressa (mineração mais rápida), Resistência, Salto, Força e, no nível 4, Regeneração ou o efeito escolhido em nível II.

## Sequência sugerida de progressão

**[Ambas]** Uma ordem que funciona para a maioria dos jogadores:
1. Madeira, ferramentas de pedra, comida, cama e abrigo.
2. Ferro: armadura e ferramentas de ferro, escudo e balde.
3. Fazenda de trigo e criação de animais.
4. Diamantes (perto de Y -59): picareta e espada de diamante.
5. Mesa de encantamentos com 15 estantes.
6. Aldeões: bibliotecário com Remendo; fazendeiros e flecheiros para esmeraldas.
7. Nether: fortaleza (varas de Blaze, verruga do Nether) e bastião (molde de netherite, ouro).
8. Poções de Resistência ao Fogo, Força e Cura.
9. Armadura e ferramentas de netherite.
10. Olhos do Ender, Fortaleza e o Ender Dragon.
11. Cidades do End: élitros e caixas de shulker.
12. Wither, Sinalizador e farms automáticas.
13. Câmaras de Provação (maça), Cidade Ancestral (Passos Furtivos) e construções grandes.

Não existe um "fim" obrigatório: depois do dragão o jogo continua livre.

---

# PARTE 3 — ENCICLOPÉDIA

## Mobs hostis do Overworld

**[Ambas]**
- **Zumbi (Zombie):** anda devagar e queima no sol. Pode dropar ferro, cenoura ou batata. Variantes: **Husk** (deserto, não queima no sol e causa Fome), **Afogado (Drowned)** (na água; pode dropar tridente ou concha de náutilo) e **Aldeão Zumbi** (pode ser curado).
- **Esqueleto (Skeleton):** atira flechas e queima no sol. Dropa ossos e flechas. Variantes: **Errante (Stray)** em biomas gelados (flechas de Lentidão), **Bogged** em pântanos e cavernas exuberantes (flechas venenosas) e **Parched** no deserto (adicionado em Mounts of Mayhem).
- **Creeper:** explode perto de você. Dropa pólvora. Gatos e jaguatiricas o afastam. Se um raio atingir um creeper, ele vira Creeper Carregado, com explosão maior.
- **Aranha (Spider):** escala paredes; neutra de dia. Dropa linha e olho de aranha. **Aranha das Cavernas (Cave Spider):** menor e venenosa; aparece em minas abandonadas e, desde a 26.2, nas Cavernas de Enxofre.
- **Enderman:** fica bravo se você olhar para os olhos dele ou atacá-lo. Teletransporta-se e foge da água. Dropa pérola do Ender.
- **Bruxa (Witch):** arremessa poções e bebe poções de cura. Dropa redstone, pólvora, açúcar, garrafas e pó de pedra luminosa.
- **Slime:** aparece em pântanos e em "chunks de slime" no subterrâneo. Divide-se em slimes menores. Dropa bolas de slime.
- **Phantom:** aparece se você passa 3 noites sem dormir. Dropa membrana.
- **Traça (Silverfish):** sai de blocos infestados em fortalezas e montanhas.
- **Saqueador (Pillager), Vingador (Vindicator), Evocador (Evoker), Devastador (Ravager), Vex:** os Illagers. Aparecem em patrulhas, postos avançados, mansões e invasões (raids). O Evocador dropa o **Totem da Imortalidade**.
- **Guardião (Guardian) e Guardião Ancião (Elder Guardian):** nos monumentos oceânicos. O Guardião Ancião causa Fadiga de Mineração.
- **Breeze:** nas Câmaras de Provação. Pula e atira cargas de vento. Dropa vara de Breeze.
- **Rangedor (Creaking):** no Jardim Pálido, à noite. Não pode ser morto diretamente: ele congela quando você olha para ele e só morre quando você destrói o **Coração de Rangedor (Creaking Heart)** ligado a ele.
- **Warden:** na Escuridão Profunda (Deep Dark). Veja a seção própria.
- **Cavaleiros (desde Mounts of Mayhem, dezembro de 2025):** Cavalo Zumbi com um zumbi armado de lança (planícies e savanas), **Camelo Husk (Camel Husk)** com um Husk e um Parched (desertos, à noite) e **Náutilo Zumbi** com um Afogado de tridente (oceanos).

## Mobs do Nether e do End

**[Ambas]** Nether:
- **Ghast:** voa e atira bolas de fogo. Dropa lágrima de Ghast (poção de Regeneração) e pólvora.
- **Blaze:** nas fortalezas. Voa e atira bolas de fogo. Dropa vara de Blaze. Bolas de neve causam dano nele.
- **Cubo de Magma (Magma Cube):** como o slime, mas imune a fogo. Dropa creme de magma.
- **Piglin:** neutro se você usar ouro. Faz escambo. **Piglin Bruto (Brute):** sempre hostil, nos bastiões.
- **Piglin Zumbificado (Zombified Piglin):** neutro, mas se você atacar um, todos por perto atacam.
- **Hoglin:** hostil, dá muita carne. Tem medo de fungos distorcidos. **Zoglin:** hoglin zumbificado.
- **Esqueleto Wither (Wither Skeleton):** nas fortalezas. Causa Murchar. Pode dropar a cabeça de esqueleto Wither (com Saque, a chance aumenta).
- **Strider:** passivo; anda sobre lava.

End:
- **Enderman:** muito comum.
- **Endermite:** às vezes aparece ao usar pérola do Ender.
- **Shulker:** nas Cidades do End. Dropa casca de shulker.
- **Ender Dragon:** o chefe do End.

## Mobs passivos e neutros

**[Ambas]**
- **Animais de fazenda:** vaca (couro, carne, leite), porco, galinha (ovos e penas), ovelha (lã; tosquie com tesoura), coelho, mooshroom (cogumelo).
- **Variantes por clima (desde 2025):** vacas, porcos e galinhas têm versões de clima temperado, quente e frio, conforme o bioma onde nascem. Galinhas de clima quente e frio botam ovos marrons e azuis.
- **Lobo, gato, jaguatirica, papagaio, raposa:** podem ser domados ou ganhar confiança.
- **Montarias:** cavalo, burro, mula, lhama, camelo, strider, náutilo e Ghast Feliz.
- **Aquáticos:** lula, lula-brilhante (glow squid), golfinho (leva você a tesouros se você alimentar com peixe), tartaruga, axolote, peixes, baiacu.
- **Neutros:** abelha (pica se o ninho for atacado), urso polar (protege filhotes), lhama (cospe), panda, cabra (dá cabeçada; dropa chifre de cabra), golfinho, Golem de Ferro.
- **Outros:** sapo (come pequenos cubos de magma e gera luzes-de-sapo), girino, Allay (pega itens iguais ao que você der para ele), farejador (Sniffer), tatu (Armadillo, dropa escamas para armadura de lobo), morcego.
- **Golem de Neve:** 2 blocos de neve + abóbora entalhada em cima.
- **Golem de Ferro:** 4 blocos de ferro em T + abóbora entalhada em cima.
- **Golem de Cobre:** bloco de cobre + abóbora entalhada em cima (desde The Copper Age).
- **Cubo de Enxofre (Sulfur Cube):** passivo; nas Cavernas de Enxofre (desde a 26.2).

## Ghast Feliz (Happy Ghast)

**[Ambas]** Adicionado no drop Chase the Skies (junho de 2025). É uma montaria voadora que leva até 4 jogadores.

Como conseguir:
1. Consiga um **Ghast Seco (Dried Ghast)**: encontrado no Vale de Areia das Almas, no Nether, ou craftado com 8 lágrimas de Ghast em volta de 1 areia das almas.
2. Coloque o Ghast Seco na água. Ele se hidrata aos poucos (cerca de 20 minutos) e vira um **Ghastinho (Ghastling)**.
3. O Ghastinho segue jogadores e cresce até virar Ghast Feliz. Dar **bolas de neve** acelera o crescimento.
4. Faça um **Arreio (Harness)** com couro, vidro e lã, e coloque no Ghast Feliz adulto para poder montá-lo.

O Ghast Feliz é pacífico, ótimo para construir no alto e para viajar em grupo.

## Golem de Cobre

**[Ambas]** Adicionado no drop The Copper Age (2025). Construa colocando uma abóbora entalhada em cima de um bloco de cobre.

O Golem de Cobre pega itens de **Baús de Cobre (Copper Chests)** e os leva para baús comuns próximos, organizando o armazenamento automaticamente. Como todo cobre, ele oxida com o tempo e fica mais lento; totalmente oxidado, vira uma estátua. Use favo de mel (honeycomb) para encerá-lo e impedir a oxidação, ou um machado para raspar a oxidação.

## Cubo de Enxofre e Cavernas de Enxofre

**[Ambas]** Adicionados no drop Chaos Cubed (26.2, junho de 2026).

**Cavernas de Enxofre (Sulfur Caves):** bioma subterrâneo do Overworld, colorido, com blocos de **enxofre** (amarelo) e **cinábrio (cinnabar)** (vermelho), espinhos de enxofre e aranhas das cavernas no lugar das aranhas comuns. Na superfície, **Fontes de Enxofre (Sulfur Springs)** indicam que há uma caverna de enxofre embaixo. As cavernas só aparecem em partes do mapa geradas depois da atualização.

**Enxofre Potente (Potent Sulfur):** gera em poças no fundo das cavernas e solta gás que causa **Náusea**. Com um bloco de magma embaixo, vira um **gêiser** que dispara de tempos em tempos, lançando jogadores, mobs e cubos para cima; com lava embaixo, o gêiser fica permanente.

**Cubo de Enxofre:** mob passivo parecido com um slime. Segure um bloco e interaja com o cubo: ele absorve o bloco e passa a ter o comportamento físico ligado àquele bloco (por exemplo, mais saltitante, mais lento ou quente). Com TNT, vira um cubo explosivo (conquista "Uh Oh"). Pode ser carregado em um balde (Balde de Cubo de Enxofre).

Outros itens do drop: blocos decorativos de enxofre e cinábrio (polidos, tijolos, cinzelados) e o disco de música "Bounce", encontrado em carrinhos com baú de minas dentro das Cavernas de Enxofre.

## Biomas principais do Overworld

**[Ambas]**
- **Planícies (Plains):** planas, com vilas e cavalos.
- **Florestas:** comum, de bétula, escura (Dark Forest, com mansões), de flores e de cerejeiras (Cherry Grove).
- **Jardim Pálido (Pale Garden):** floresta cinzenta com o Rangedor e o Coração de Rangedor.
- **Floresta Matizada (Dappled Forest):** floresta outonal com choupos vermelhos, laranjas e amarelos (desde a 26.3).
- **Taiga e Taiga Nevada:** pinheiros, raposas e lobos.
- **Selva (Jungle):** templos, papagaios, jaguatiricas, pandas, cacau e melancias.
- **Deserto:** vilas, pirâmides, husks, camelos e coelhos.
- **Savana:** acácias, vilas, cavalos e lhamas.
- **Terras Áridas (Badlands):** terracota colorida, muito ouro e minas abandonadas na superfície.
- **Pântano e Pântano de Mangue:** slimes, sapos, cabanas de bruxa.
- **Montanhas (picos, encostas, prados):** esmeraldas, cabras e muito ferro.
- **Oceanos:** quente, morno, frio, congelado e profundo. Monumentos, naufrágios e ruínas.
- **Ilhas de Cogumelo:** mooshrooms; monstros não aparecem.
- **Biomas de caverna:** Cavernas Exuberantes (axolotes, frutinhas brilhantes, azaleia), Cavernas de Espeleotemas (muito cobre), Escuridão Profunda (Warden) e Cavernas de Enxofre.

## Estruturas do Overworld

**[Ambas]**
- **Vila (Village):** aldeões, ferreiro com baú, camas e plantações.
- **Templo do Deserto (Desert Pyramid):** baús com diamantes, ouro e esmeraldas no subsolo. **Cuidado:** a placa de pressão no centro ativa TNT. Tem areia suspeita para arqueologia.
- **Templo da Selva:** armadilhas com flechas e um baú escondido.
- **Monumento Oceânico:** guardiões, 3 Guardiões Anciões e 8 blocos de ouro. Leve poção de Respiração Aquática.
- **Mansão da Floresta (Woodland Mansion):** na Floresta Escura. Evocadores (totens) e vingadores.
- **Posto Avançado de Saqueadores (Pillager Outpost):** torre com saqueadores; às vezes tem jaulas com um Golem de Ferro ou Allays presos.
- **Mina Abandonada (Mineshaft):** túneis de madeira com carrinhos com baú e aranhas das cavernas.
- **Masmorra (Dungeon):** sala de pedregulho musgoso com um gerador de mobs (spawner) e baús.
- **Fortaleza (Stronghold):** onde fica o portal do End.
- **Naufrágio (Shipwreck)** e **Ruínas Oceânicas:** mapas do tesouro que levam ao **Tesouro Enterrado (Buried Treasure)**, que tem o Coração do Mar.
- **Iglu:** às vezes tem um porão secreto com um aldeão zumbi para curar.
- **Ruínas de Trilha (Trail Ruins):** arqueologia, cacos de cerâmica e moldes de acabamento.
- **Cidade Ancestral (Ancient City):** na Escuridão Profunda.
- **Câmaras de Provação (Trial Chambers):** veja a seção própria.
- **Acampamento Abandonado (Abandoned Camp):** desde a 26.3. Veja a seção do drop Wilderness Bound.
- **Portal em Ruínas:** espalhados pelo mundo, com baús com itens de ouro.

## Câmaras de Provação (Trial Chambers)

**[Ambas]** Adicionadas na atualização Tricky Trials (1.21, 2024). São complexos subterrâneos de cobre e tufo (tuff), geralmente entre Y -40 e Y -20.

- **Gerador de Provação (Trial Spawner):** gera ondas de mobs; quanto mais jogadores perto, mais mobs. Quando você vence, ele solta recompensas e **Chaves de Provação (Trial Keys)**.
- **Cofre (Vault):** abre com uma Chave de Provação e dá um saque para cada jogador.
- **Modo Sinistro (Ominous):** se você entrar com o efeito **Mau Presságio (Bad Omen)**, ganha o **Presságio de Provação (Trial Omen)** e os geradores ficam mais difíceis. Eles soltam **Chaves de Provação Sinistras**, que abrem os **Cofres Sinistros**, com itens melhores, como o **Núcleo Pesado (Heavy Core)**.
- **Breeze:** mob exclusivo; dropa vara de Breeze.
- **Recompensas:** cargas de vento, garrafas sinistras, moldes de acabamento Flow e Bolt, o disco "Creator", maçãs douradas encantadas e livros encantados (como Densidade, Ruptura e Rajada de Vento).

**Maça (Mace):** 1 Núcleo Pesado + 1 vara de Breeze. O dano aumenta com a altura da queda antes do golpe. Combine com cargas de vento para pular alto e cair batendo.

**Carga de Vento (Wind Charge):** 1 vara de Breeze vira 4 cargas. Arremesse para dar um super salto, empurrar mobs ou abrir portas à distância.

## Escuridão Profunda, Cidade Ancestral e Warden

**[Ambas]** A **Escuridão Profunda (Deep Dark)** é um bioma de caverna muito fundo, perto do fundo do mundo, coberto de **sculk**. A **Cidade Ancestral (Ancient City)** fica dentro dela.

- **Sensores de Sculk** captam vibrações (passos, blocos quebrados, flechas). **Gritadores de Sculk (Sculk Shriekers)** dão o efeito Escuridão e, após 3 ativações, invocam o **Warden**.
- **Warden:** cego, encontra você por vibração e por cheiro. Tem muita vida e golpes que podem matar mesmo com armadura de netherite. Também tem um ataque sônico que atravessa paredes e escudos. **Não lute com ele; fuja ou evite chamá-lo.**
- Como explorar: ande agachado (agachar não gera vibração), coloque lã sobre os sensores ou ande sobre lã/tapete, e jogue bolas de neve ou flechas para distraí-lo.
- **Saque:** livros de **Passos Furtivos (Swift Sneak)**, maçãs douradas encantadas, **fragmentos de eco (Echo Shards)**, fragmentos de disco (5 fragmentos = disco "5"), moldes de acabamento Silence e Ward, e selas.
- **Bússola de Recuperação (Recovery Compass):** 1 bússola + 8 fragmentos de eco. Aponta para onde você morreu pela última vez.

## Arqueologia

**[Ambas]**
- **Pincel (Brush):** 1 pena + 1 barra de cobre + 1 graveto.
- Use o pincel em **areia suspeita** ou **cascalho suspeito** (blocos com textura levemente diferente), encontrados em pirâmides do deserto, poços de deserto, ruínas oceânicas e ruínas de trilha. Escavar com picareta destrói o item.
- **Cacos de Cerâmica (Pottery Sherds):** 4 cacos (ou tijolos) formam um **Vaso Decorado (Decorated Pot)** com desenhos.
- **Ovo de Farejador:** nas ruínas oceânicas quentes. Choca e vira um farejador, que cava sementes antigas de **flor-tocha (torchflower)** e **planta-jarro (pitcher plant)**.

## Moldes de ferraria e acabamentos de armadura

**[Ambas]** **Moldes de Ferraria (Smithing Templates)** são usados na Mesa de Ferraria.
- **Molde de Melhoria de Netherite:** transforma diamante em netherite. Fica nos bastiões.
- **Moldes de Acabamento (Armor Trims):** decoram armaduras com padrões e cores (a cor vem do material: ferro, cobre, ouro, lápis, esmeralda, diamante, netherite, redstone, ametista, quartzo ou resina). Encontrados em estruturas: Sentry (posto de saqueadores), Dune (pirâmide do deserto), Coast (naufrágio), Wild (templo da selva), Ward e Silence (cidade ancestral), Vex (mansão), Tide (Guardião Ancião), Snout (bastião), Rib (fortaleza do Nether), Eye (fortaleza), Spire (cidade do End), Wayfinder, Raiser, Shaper e Host (ruínas de trilha), Flow e Bolt (câmaras de provação).
- Para copiar qualquer molde: 1 molde + 7 diamantes + o bloco base do molde (por exemplo, arenito para Dune).

## Itens raros e onde conseguir

**[Ambas]**
- **Totem da Imortalidade:** Evocadores (mansões e invasões). Segurado na mão, impede uma morte.
- **Élitros:** Navios do End.
- **Tridente:** Afogados (drop raro). Não é craftável.
- **Coração do Mar:** Tesouro Enterrado. Com 8 conchas de náutilo vira um **Conduíte**, que dá respiração e visão debaixo d'água.
- **Estrela do Nether:** Wither.
- **Maçã Dourada Encantada:** baús de várias estruturas e cofres sinistros.
- **Selas:** baús, pesca, mercadores; desde 2025 também craftáveis com couro e ferro.
- **Cabeça de Esqueleto Wither:** Esqueletos Wither.
- **Etiqueta de Nome (Name Tag):** craftável desde a 26.1; também em baús, pesca e com bibliotecários.
- **Núcleo Pesado:** Cofres Sinistros.
- **Ovo do Dragão:** um por mundo, após o primeiro dragão.
- **Livros de Remendo:** bibliotecários, pesca e baús.

## Armazenamento

**[Ambas]**
- **Baú (Chest):** 8 tábuas; 27 espaços. Dois baús lado a lado formam um baú duplo com 54 espaços.
- **Barril (Barrel):** 27 espaços; pode ter um bloco em cima e continuar abrindo.
- **Baú do Ender (Ender Chest):** 8 obsidianas + 1 olho do Ender. O conteúdo é o mesmo em todos os Baús do Ender do jogador, em qualquer lugar ou dimensão.
- **Caixa de Shulker:** portátil; guarda os itens ao ser quebrada.
- **Saco (Bundle):** guarda vários tipos de itens em um espaço do inventário; pode ser tingido.
- **Baú de Cobre:** usado pelo Golem de Cobre para organizar itens.
- **Funil (Hopper):** move itens para dentro e para fora de contêineres; base de sistemas de organização.
- **Estante (Shelf):** bloco decorativo para exibir itens (The Copper Age).

## Navegação e localização

**[Ambas]**
- **Bússola:** aponta para o ponto de nascimento do mundo. Usada em um **Magnetita (Lodestone)**, aponta para essa magnetita.
- **Bússola de Recuperação:** aponta para o local da sua última morte.
- **Mapa:** 9 papéis (ou papel + bússola para o mapa localizador). Pode ser ampliado na mesa de cartografia. **Mapas de Exploração** levam a estruturas; vêm de cartógrafos e, desde a 26.3, também de Acampamentos Abandonados.
- **Barra Localizadora (Locator Bar):** desde 2025, mostra na tela a direção dos outros jogadores no multiplayer.
- **Luneta (Spyglass):** 2 barras de cobre + 1 fragmento de ametista; aproxima a visão.
- **Coordenadas:** anote as da base e dos portais.

## Transporte

**[Ambas]**
- **A pé ou correndo:** pular enquanto corre é mais rápido.
- **Barco:** muito rápido na água e mais rápido ainda no gelo compactado ou gelo azul. Leva 2 mobs ou jogadores; versão com baú.
- **Carrinho de Mina (Minecart):** em trilhos. Trilhos energizados (com ouro e redstone) aceleram.
- **Cavalos e camelos:** rápidos em terra.
- **Élitros com foguetes:** o mais rápido para longas distâncias.
- **Ghast Feliz:** voo calmo para até 4 jogadores.
- **Nether:** cada bloco lá equivale a 8 no Overworld; jogadores constroem "rodovias" no teto do Nether.
- **Pérola do Ender:** teletransporte curto (causa um pouco de dano).
- **Tridente com Correnteza:** lança o jogador na chuva ou na água.

## Mecânicas de combate

**[Java]** Desde a versão 1.9, cada arma tem um **tempo de recarga** de ataque: bater sem esperar a recarga causa pouco dano. A espada é rápida; o machado é lento e forte e **desativa escudos** por alguns segundos. **Golpe crítico:** atacar enquanto cai depois de um pulo causa 50% a mais de dano. A espada faz ataque de varredura em mobs próximos.

**[Bedrock]** Não existe tempo de recarga de ataque: clicar rápido funciona. O machado causa menos dano que a espada. Críticos também existem ao cair após o pulo.

**[Ambas]**
- **Escudo:** 6 tábuas + 1 barra de ferro. Bloqueia ataques de frente, flechas e explosões de creeper.
- **Arco:** segure para carregar; puxado ao máximo causa mais dano. **Besta (Crossbow):** pode disparar foguetes, que explodem.
- **Recuo:** acertar enquanto corre empurra mais longe.
- **Efeitos:** Força aumenta o dano; Fraqueza diminui; Resistência reduz o dano recebido.

## Armas

**[Ambas]**
- **Espada:** arma padrão.
- **Machado:** ferramenta e arma; **[Java]** dano alto e desativa escudos.
- **Arco e Besta:** à distância. Flechas: pederneira + graveto + pena = 4 flechas. **Flechas com efeito:** 8 flechas em volta de uma poção persistente.
- **Tridente:** corpo a corpo ou arremessado; não craftável.
- **Maça (Mace):** dano baseado na altura da queda. Feita com Núcleo Pesado + vara de Breeze.
- **Lança (Spear):** adicionada em Mounts of Mayhem (dezembro de 2025). Existe em vários materiais, de madeira até netherite, com alcance maior que a espada. Tem um ataque de estocada que se beneficia do movimento, inclusive montado a cavalo. Encantamento exclusivo: **Investida (Lunge)**.

## Morte, renascimento e recuperação de itens

**[Ambas]** Quando você morre, todos os itens e parte do XP caem no chão. Os itens **desaparecem depois de 5 minutos** se a área estiver carregada (com um jogador por perto). Você renasce na última cama ou âncora de renascimento usada, ou no ponto de nascimento do mundo.

- Anote as coordenadas da morte (aparecem na tela de morte em algumas versões) ou use a **Bússola de Recuperação**.
- Itens com **Maldição do Desaparecimento** somem.
- **Âncora de Renascimento (Respawn Anchor):** define o renascimento no Nether; carrega com pedra luminosa. Explode se for usada fora do Nether.
- A **Cama de Palha (Straw Bed)**, da 26.3, deixa pular a noite sem mudar seu ponto de renascimento.
- Regra de jogo para não perder itens: veja "Comandos úteis".

## Redstone: componentes

**[Ambas]**
- **Pó de Redstone:** carrega sinal por até 15 blocos.
- **Fontes de sinal:** alavanca (liga/desliga), botão (pulso curto), placa de pressão, placa de pressão com peso, gancho de armadilha com linha, sensor de luz do dia, bloco de redstone, alvo (target block), tocha de redstone e sensor de sculk.
- **Tocha de Redstone:** fica ligada e se desliga quando o bloco onde está recebe sinal (inverte o sinal).
- **Repetidor (Repeater):** renova o sinal para 15, cria atraso e só deixa o sinal passar em uma direção.
- **Comparador (Comparator):** compara sinais, subtrai sinais e mede quanto um contêiner está cheio.
- **Observador (Observer):** emite um pulso quando o bloco à frente dele muda. Essencial em farms automáticas.
- **Pistão e Pistão Grudento (Sticky Piston):** empurram blocos (até 12); o grudento puxa de volta.
- **Liberador (Dispenser):** usa ou dispara o item (flechas, água, lava, farinha de osso). **Ejetor (Dropper):** só solta o item.
- **Funil (Hopper):** transporta itens; para quando recebe sinal de redstone.
- **Lâmpada de Cobre (Copper Bulb):** liga ou desliga a cada pulso (memória).
- **Fabricador (Crafter):** crafta automaticamente quando recebe pulso, seguindo a receita colocada nele.
- **Bloco de Notas (Note Block):** toca notas; o instrumento depende do bloco embaixo. Desde a 26.1, blocos de cobre embaixo dão som de trompete.
- **Trilho Detector, Trilho Ativador e Trilho Energizado:** para carrinhos.

## Redstone: diferenças entre Java e Bedrock

- **[Java]** Existe a **quase-conectividade**: pistões, liberadores e ejetores podem ser ativados por sinal no bloco acima deles. Muitos circuitos dependem disso.
- **[Bedrock]** Não existe quase-conectividade.
- **[Java]** Pistões não movem baús, fornalhas e outros contêineres.
- **[Bedrock]** Pistões **movem** contêineres com os itens dentro.
- **[Java]** Pistões grudentos com pulso muito curto "cospem" o bloco.
- **[Bedrock]** A ordem de atualização da redstone pode variar, então circuitos muito precisos da Java nem sempre funcionam.
- Por isso, **tutoriais de farms são específicos de cada edição**. Sempre confira se o tutorial é para Java ou Bedrock.

## Comandos úteis e regras de jogo

**[Ambas]** Comandos precisam de cheats ativados. **[Java]** Em um mundo sem cheats, use "Abrir para LAN" e ative "Permitir comandos". **[Bedrock]** Ativar cheats desliga as conquistas daquele mundo.

- `/gamemode survival|creative|adventure|spectator` — muda o modo de jogo.
- `/time set day` — vira dia. `/weather clear` — tempo limpo.
- `/tp <x> <y> <z>` — teletransporta.
- `/locate structure <nome>` — mostra as coordenadas da estrutura mais próxima (exemplo: `village_plains`, `stronghold`, `trial_chambers`). `/locate biome <nome>` — idem para biomas.
- `/give @s <item> <quantidade>` — dá itens.
- `/seed` — mostra a semente do mundo. **[Bedrock]** a semente aparece nas configurações do mundo.
- `/difficulty <nível>` e `/kill @e[type=<mob>]`.
- **Manter inventário ao morrer:** `/gamerule keepInventory true`. Em versões recentes da Java os nomes das regras de jogo podem aparecer em outro formato (por exemplo, com underline); use a tecla Tab para autocompletar.
- Outras regras: `doDaylightCycle` (parar o tempo), `doMobSpawning`, `doFireTick`, `mobGriefing` (impede creepers de destruir blocos e endermen de pegar blocos), `playersSleepingPercentage` **[Java]**.

---

# PARTE 4 — ATUALIZAÇÕES RECENTES (2024 A 2026)

## Linha do tempo das atualizações recentes

**[Ambas]** Do mais antigo para o mais recente (números da Java Edition):
- **1.21 — Tricky Trials** (junho de 2024): Câmaras de Provação, Breeze, maça, cargas de vento, Fabricador, Lâmpada de Cobre, blocos de tufo e cobre decorativos.
- **1.21.2 — Bundles of Bravery** (outubro de 2024): Sacos (bundles) liberados para todos.
- **1.21.4 — The Garden Awakens** (dezembro de 2024): Jardim Pálido, Rangedor, Coração de Rangedor, resina e tijolos de resina, flor olho-de-pálpebra (eyeblossom).
- **1.21.5 — Spring to Life** (março de 2025): variantes de vaca, porco e galinha por clima; arbusto de vagalumes, folhas no chão (leaf litter), flores silvestres (wildflowers), flor de cacto, grama seca; folhas caindo das árvores.
- **1.21.6 — Chase the Skies** (junho de 2025): Ghast Feliz, Ghast Seco, Ghastinho, Arreio e Barra Localizadora.
- **1.21.9 — The Copper Age** (2025): Golem de Cobre, Baú de Cobre, Estante, ferramentas e armaduras de cobre, tocha de cobre e novos blocos de cobre.
- **1.21.11 — Mounts of Mayhem** (dezembro de 2025): Lança, Náutilo e Náutilo Zumbi, Camelo Husk, Parched, cavalos zumbis aparecendo naturalmente, armadura de náutilo e armadura de cavalo de netherite.
- **26.1 — Tiny Takeover** (março de 2026).
- **26.2 — Chaos Cubed** (junho de 2026).
- **26.3 — Wilderness Bound** (setembro de 2026).

## Mounts of Mayhem (1.21.11, dezembro de 2025)

**[Ambas]** Drop focado em montarias e combate montado. Foi a última versão com a numeração antiga "1.x".
- **Lança (Spear):** nova arma em vários materiais, com estocada que aproveita o movimento; encantamento exclusivo Investida (Lunge).
- **Náutilo (Nautilus):** montaria aquática que pode ser domada; usa **armadura de náutilo**.
- **Náutilo Zumbi:** aparece com um Afogado de tridente montado; só é hostil quando montado por um mob hostil. Tem a variante coral nos oceanos quentes.
- **Cavalo Zumbi:** agora aparece naturalmente à noite em planícies e savanas, com um zumbi de lança montado. Depois de derrubar o cavaleiro, dá para domar, selar e colocar armadura (a armadura protege o cavalo zumbi do sol).
- **Camelo Husk:** camelo morto-vivo que aparece à noite em desertos com dois cavaleiros: um Husk com lança e um **Parched**.
- **Parched:** nova variante de esqueleto do deserto.
- **Armadura de cavalo de netherite:** melhoria da armadura de diamante na mesa de ferraria.

## Tiny Takeover (26.1, março de 2026)

**[Ambas]** Primeiro drop de 2026 e primeiro com a numeração por ano. Na Bedrock saiu como 26.10.
- **Filhotes redesenhados:** quase todos os filhotes de mobs ganharam modelos, texturas e, em alguns casos, sons novos (lobo, gato, porco, cavalo, galinha, entre outros).
- **Dente-de-leão Dourado (Golden Dandelion):** 1 dente-de-leão cercado por 8 pepitas de ouro. Use em um filhote para **impedir que ele cresça**; use de novo para ele voltar a crescer. **[Java]** Não funciona em filhotes mortos-vivos nem em aldeões bebês.
- **Etiquetas de nome craftáveis** na mesa de trabalho.
- **Som de trompete** no bloco de notas com blocos de cobre embaixo.
- **Cortador de pedras:** conversões diretas entre variantes de pedra e ardósia profunda.
- **[Java]** Servidores passam a exigir Java 25.

## Chaos Cubed (26.2, junho de 2026)

**[Ambas]** Segundo drop de 2026, lançado em 16 de junho de 2026 (Bedrock 26.30).
- **Cavernas de Enxofre:** novo bioma subterrâneo com enxofre, cinábrio, espinhos de enxofre, poças de enxofre potente (Náusea) e aranhas das cavernas.
- **Gêiseres:** enxofre potente com magma embaixo dispara periodicamente; com lava embaixo, dispara sem parar. Lançam jogadores, mobs e cubos para o alto. Sensores de sculk detectam erupções.
- **Fontes de Enxofre** na superfície indicam uma caverna embaixo.
- **Cubo de Enxofre:** mob passivo que absorve blocos e muda de comportamento físico. Com TNT, vira explosivo.
- **Blocos novos:** famílias decorativas de enxofre e cinábrio.
- **Disco "Bounce"** em carrinhos com baú das minas dentro das cavernas de enxofre.
- **[Java]** **Lista de Amigos** embutida e **renderizador Vulkan experimental**.

## Wilderness Bound (26.3, setembro de 2026)

**[Ambas]** Terceiro drop de 2026, lançado em 15 de setembro de 2026 nas duas edições. Focado em exploração.
- **Floresta Matizada (Dappled Forest):** bioma outonal em regiões mais frias, com grama alaranjada, troncos caídos e choupos.
- **Choupo (Poplar):** nova família de madeira (troncos e tábuas cinza quentes). As folhas podem ser vermelhas, laranjas ou amarelas, e a mesma muda pode crescer com qualquer uma das três cores. Inclui barco e barco com baú de choupo.
- **Cogumelo-prateleira (Shelf Mushroom):** cresce nas laterais de troncos de choupo, em versão pequena e grande (farinha de osso faz crescer). É **saltitante** e serve para ensopado de cogumelo e ensopado suspeito.
- **Arbusto Vermelho (Red Shrub):** só na Floresta Matizada; mantém a cor vermelha em qualquer bioma; pode ir para a composteira.
- **Acampamento Abandonado (Abandoned Camp):** estrutura encontrada em vários biomas (prados, cerejeiras, florestas, taigas, selvas, pântanos, savanas, terras áridas arborizadas, jardim pálido e outros), com visual adaptado a cada um. Tem barris, baús e **baús secretos** com itens de começo de jogo: armas de cobre, bússolas, pólvora, camas de palha e **Mapas de Exploração**.
- **Mapas de Exploração novos:** apontam para acampamentos abandonados, mansões, monumentos e, nos baús secretos, para cidades ancestrais, minas e pirâmides do deserto.
- **Almofada (Cushion):** 3 lajes de lã da mesma cor. Permite **sentar**. Existe em 16 cores e fica sobre superfícies planas.
- **Cama de Palha (Straw Bed):** 3 fardos de feno. Pula a noite **sem mudar o ponto de renascimento**, mas quebra depois de um uso. Aldeões não usam. Explode no Nether.
- **Escadas e lajes de lã:** 16 cores; abafam vibrações como a lã (úteis perto do Warden).
- **Escadas e lajes de concreto:** 16 cores; craftáveis ou feitas no cortador de pedras.
- **Gráficos:** Transparência Independente de Ordem (OIT) melhora a renderização de objetos translúcidos.

## O que vem por aí: drop de inverno (26.4, em teste)

**[Ambas]** Em outubro de 2026 o quarto drop do ano ainda **não foi lançado**; está em snapshots (Java) e previews (Bedrock). O conteúdo pode mudar. O que está em teste:
- **Cavernas de Gelo (Ice Caves):** novo bioma subterrâneo com cristais de gelo e estalactites de gelo (icicles).
- **Frostbite:** variante de zumbi que arremessa bolas de gelo.
- **Efeito Congelamento** e uma poção ligada a ele.
- Pequenas mudanças, como neve colocável em gelo compactado e bolas de neve empurrando jogadores.
- **[Java]** O Vulkan passa a ser o renderizador padrão nos snapshots.

O lançamento é esperado para dezembro de 2026, mas a data e o nome oficial ainda não foram anunciados.

---

# PARTE 5 — AVANÇADO: FARMS E TÉCNICAS

## Princípios de farms (fazendas automáticas)

**[Ambas]**
- **Chunks carregados:** farms só funcionam com um jogador por perto (ou com chunks carregados). Construa perto da base.
- **Distâncias de spawn:** **[Java]** mobs hostis aparecem a pelo menos 24 blocos do jogador e somem (despawn) a mais de 128 blocos. **[Bedrock]** o spawn depende da "distância de simulação" configurada no mundo.
- **Limite de mobs (mob cap):** existe um número máximo de mobs hostis ao mesmo tempo. Iluminar cavernas próximas ou construir a farm no alto (sobre o oceano) faz os mobs aparecerem só na farm.
- **Coleta de itens:** funis embaixo de lajes ou de trilhos com carrinho-funil levam os drops para baús.
- **Tutoriais:** mecânicas mudam entre edições e versões. Procure tutoriais para a sua edição e versão exatas.

## Farm de ferro

**[Java]** Golems de Ferro aparecem quando **aldeões entram em pânico** perto de um zumbi. A farm clássica tem 3 ou mais aldeões presos com camas e blocos de trabalho, um zumbi preso onde eles possam vê-lo e uma plataforma onde os golens aparecem e caem em lava (ou em outro mecanismo), com funis coletando o ferro e as papoulas.

**[Bedrock]** Golems aparecem em vilas com uma quantidade suficiente de aldeões e camas, não por pânico. As farms de ferro da Bedrock costumam ter muitos aldeões e camas, e o design é diferente do da Java.

## Farm de mobs e de experiência

**[Ambas]**
- **Farm de sala escura (dark room):** plataformas escuras no alto, onde mobs aparecem e são empurrados por água até um buraco. Uma queda de cerca de 22 blocos deixa zumbis e esqueletos quase sem vida; um golpe finaliza e dá o XP. Rende ossos, flechas, pólvora, linha e carne podre.
- **Farm de gerador (spawner):** use o gerador de uma masmorra (zumbi, esqueleto, aranha). Mantenha o gerador no escuro e empurre os mobs com água até um ponto de abate.
- **Farm de Enderman (no End):** **[Java]** uma plataforma a mais de 128 blocos da ilha central, com Endermites como isca, rende muito XP e pérolas.
- **XP sem farm:** derreter cactos ou alga em fornalhas e minerar quartzo do Nether também dão XP.

## Farms de plantações automáticas

**[Ambas]**
- **Cana-de-açúcar, abóbora e melancia:** um **observador** detecta quando a planta cresce e ativa um **pistão** que quebra o bloco; funis coletam.
- **Bambu e algas:** observadores com pistões (algas crescem rápido e servem de combustível como bloco de alga seca).
- **Fazenda com aldeões fazendeiros:** aldeões fazendeiros colhem e replantam sozinhos e jogam as plantações para outros aldeões; um funil embaixo de um aldeão coleta parte delas.
- **Farinha de osso automática:** composteira alimentada por funil com restos de plantas.

## Farm de ouro e escambo automático

**[Java]** No **teto do Nether** (acima da bedrock, a partir de Y 128), plataformas de bloco de magma geram piglins zumbificados. Ovos de tartaruga atraem esses mobs para um ponto de queda. Rende ouro, pepitas e muito XP.

**[Ambas]** Escambo automático: um piglin preso recebe barras de ouro por um ejetor e os itens que ele devolve caem em funis. Rende pérolas do Ender, obsidiana, linha e poções de Resistência ao Fogo.

O design exato da farm de ouro muda entre Java e Bedrock.

## Invasões (raids) e farm de invasões

**[Ambas]**
- **Mau Presságio (Bad Omen):** desde 2024, o efeito vem de beber uma **Garrafa Sinistra (Ominous Bottle)**, que cai do capitão de uma patrulha ou de um posto de saqueadores (o capitão tem um estandarte na cabeça).
- Entrar em uma vila com Mau Presságio dá o efeito **Presságio de Invasão (Raid Omen)**, e a invasão começa em seguida.
- Vença todas as ondas para ganhar o efeito **Herói da Vila**, que dá descontos com os aldeões.
- **Farm de invasões:** estruturas que capturam os illagers em uma área de abate. Rendem esmeraldas, **Totens da Imortalidade**, selas, pólvora, redstone e garrafas sinistras.

## Técnicas e truques úteis

**[Ambas]**
- **Balde de água na queda (MLG):** coloque água no chão logo antes de cair para anular o dano de queda; recolha a água depois.
- **Pilar de blocos:** pule e coloque um bloco embaixo para subir rápido ou fugir de mobs.
- **Fardo de feno e blocos de slime/mel:** reduzem ou anulam dano de queda.
- **Pontes:** ande agachado para trás na beirada e coloque blocos na frente.
- **Camas no Nether:** explodem; usadas para minerar detrito ancestral, com cuidado.
- **Portas de ferro** só abrem com redstone (botão, alavanca ou placa de pressão); mobs não conseguem abri-las.
- **Iluminação:** iluminar toda a área de uma base impede monstros.
- **Tesoura em abóbora:** cria abóbora entalhada (para golens e para usar na cabeça no End).
- **Fogo em cima de netherrack** queima para sempre (útil para lareiras).

---

# PARTE 6 — DIFERENÇAS ENTRE JAVA E BEDROCK (RESUMO)

## Tabela de diferenças entre Java e Bedrock

| Tema | Java | Bedrock |
| --- | --- | --- |
| Plataformas | PC (Windows, macOS, Linux) | Windows, consoles, celulares |
| Crossplay | Só com Java | Entre todas as plataformas Bedrock |
| Mods | Comunidade grande (Fabric, Forge, NeoForge) | Add-ons e Marketplace |
| Combate | Tempo de recarga de ataque; machado forte que desativa escudo | Sem recarga; clicar rápido funciona |
| Golpe de Varredura | Existe | Não existe |
| Mão secundária | Qualquer item | Apenas alguns itens |
| Coordenadas | F3 | Opção "Mostrar coordenadas" |
| Quase-conectividade | Existe | Não existe |
| Pistões e contêineres | Não movem baús | Movem baús com os itens |
| Spawn de mobs | Entre 24 e 128 blocos do jogador | Depende da distância de simulação |
| Farm de ferro | Por pânico de aldeões | Por tamanho da vila (aldeões e camas) |
| Wither | Vida padrão | Mais vida e ataque de investida |
| Poção de Decomposição | Não existe | Existe (só por comando/Criativo) |
| Empalamento (Impaling) | Dano extra só contra mobs aquáticos | Dano extra contra qualquer mob molhado (na água ou na chuva) |
| Conquistas | Avanços (advancements) | Conquistas (achievements) Xbox; desativadas com cheats |
| Numeração | 26.1, 26.2, 26.3... | 26.10, 26.30... |

Ambas recebem os mesmos drops de conteúdo no mesmo dia na maioria das vezes, mas com detalhes de mecânica diferentes.

---

# PARTE 7 — PERGUNTAS FREQUENTES

## Perguntas frequentes sobre o começo do jogo

**Qual a primeira coisa a fazer no Minecraft?** Pegar madeira com a mão, fazer a mesa de trabalho e uma picareta de madeira, depois ferramentas de pedra, e então conseguir comida e abrigo antes da noite.

**Como fazer uma mesa de trabalho?** 4 tábuas em quadrado no inventário. 1 tronco dá 4 tábuas.

**Como fazer tochas?** 1 carvão (ou carvão vegetal) em cima de 1 graveto. Rende 4 tochas.

**Como fazer carvão vegetal?** Coloque troncos na fornalha com qualquer combustível.

**Como fazer uma cama?** 3 lãs da mesma cor em cima de 3 tábuas. Lã vem de ovelhas (tesoura ou matando) ou de linha (4 linhas = 1 lã).

**Por que não consigo dormir?** Só é possível dormir à noite ou em tempestades, sem monstros por perto. No Nether e no End a cama explode.

**Como não morrer na primeira noite?** Faça um abrigo fechado com tocha dentro, ou cave numa encosta e feche a entrada.

## Perguntas frequentes sobre mineração

**Em que altura encontrar diamantes?** Entre Y 16 e Y -64, mais comuns quanto mais fundo; a melhor altura é perto de Y -59. Precisa de picareta de ferro ou melhor.

**Em que altura encontrar ferro?** Perto de Y 16 e também no alto das montanhas.

**Em que altura encontrar ouro?** Perto de Y -16, ou na superfície das Terras Áridas (Badlands).

**Em que altura encontrar redstone e lápis?** Redstone abaixo de Y 15, mais comum lá embaixo. Lápis perto de Y 0.

**Onde fica o detrito ancestral (netherite)?** No Nether, mais comum perto de Y 15.

**Como pegar obsidiana?** Água sobre uma fonte de lava forma obsidiana. Minere com picareta de diamante ou netherite.

**Qual a picareta para cada minério?** Pedra/cobre: ferro, cobre, lápis. Ferro: ouro, redstone, diamante, esmeralda. Diamante: obsidiana e detrito ancestral.

## Perguntas frequentes sobre o Nether e o End

**Como fazer o portal do Nether?** Moldura de obsidiana de 4 de largura por 5 de altura (no mínimo 10 obsidianas sem os cantos), acesa com isqueiro.

**Como achar uma fortaleza do Nether?** Explore em linha reta com poções de Resistência ao Fogo, procurando construções grandes de tijolos escuros do Nether. Com cheats ativos, `/locate structure fortress` mostra a mais próxima.

**Como evitar que os piglins me ataquem?** Use pelo menos uma peça de armadura de ouro e não abra baús perto deles.

**Como achar o portal do End?** Jogue olhos do Ender (pérola do Ender + pó de Blaze); eles voam para a Fortaleza (Stronghold). Precisa de 12 olhos no portal.

**Como derrotar o Ender Dragon?** Destrua todos os Cristais do End nos pilares, depois ataque o dragão quando ele pousar no portal. Leve arco, blocos, comida e abóbora entalhada na cabeça.

**Onde estão os élitros?** Nos Navios do End, perto das Cidades do End nas ilhas externas. Chegue lá pelo Portal de Passagem do End depois de derrotar o dragão.

## Perguntas frequentes sobre encantamentos e itens

**Como conseguir Remendo (Mending)?** Com aldeões bibliotecários, pescando ou em baús. Não sai na mesa de encantamentos.

**Como encantar no nível 30?** 15 estantes de livros em volta da mesa, com 1 bloco de ar entre elas e a mesa.

**Fortuna ou Toque de Seda?** Fortuna multiplica minérios como diamante. Toque de Seda pega o bloco inteiro. Não podem estar na mesma ferramenta.

**Como fazer netherite?** 4 fragmentos (do detrito ancestral derretido) + 4 barras de ouro = 1 barra; depois mesa de ferraria com o Molde de Melhoria de Netherite e o item de diamante.

**Como fazer a maça?** Núcleo Pesado (dos Cofres Sinistros das Câmaras de Provação) + vara de Breeze.

**Como fazer uma poção de Resistência ao Fogo?** Garrafa de água + verruga do Nether = Poção Estranha; depois adicione creme de magma.

## Perguntas frequentes sobre as novidades de 2026

**Qual é a versão mais recente do Minecraft?** Em outubro de 2026, a Java Edition 26.3 (Wilderness Bound, lançada em 15 de setembro de 2026), com o mesmo conteúdo na Bedrock. O drop de inverno (26.4) ainda está em teste.

**Existe Minecraft 1.22?** Não. Depois da 1.21.11 a numeração mudou para o ano: 26.1, 26.2, 26.3.

**O que faz o Dente-de-leão Dourado?** Impede um filhote de crescer. Receita: dente-de-leão + 8 pepitas de ouro.

**O que é o Cubo de Enxofre?** Um mob passivo das Cavernas de Enxofre (26.2) que absorve o bloco que você der para ele e muda de comportamento físico.

**Como fazer um gêiser?** Coloque magma embaixo de um bloco de Enxofre Potente (dispara de tempos em tempos) ou lava (dispara sem parar).

**Como sentar no Minecraft?** Desde a 26.3, com a Almofada (3 lajes de lã da mesma cor).

**O que é a Cama de Palha?** Cama da 26.3 feita com 3 fardos de feno. Pula a noite sem mudar o renascimento, mas quebra depois de um uso.

**Onde fica a Floresta Matizada?** Em regiões mais frias do Overworld; tem choupos vermelhos, laranjas e amarelos. Só aparece em áreas do mapa geradas depois da 26.3.

---

## Glossário

- **Bioma:** região do mundo com clima, vegetação e mobs próprios.
- **Bedrock (bloco):** rocha indestrutível no fundo do mundo e no teto do Nether. Não confundir com a Bedrock Edition.
- **Chunk:** área de 16 x 16 blocos usada pelo jogo para carregar o mundo.
- **Craftar:** fabricar um item na grade de crafting.
- **Drop (de mob):** item que um mob deixa ao morrer. **Game drop:** atualização de conteúdo lançada a cada poucos meses.
- **Farm:** construção que gera recursos automaticamente.
- **Hotfix:** pequena atualização de correção (por exemplo, 26.3.1).
- **Mob:** qualquer criatura do jogo (de "mobile entity").
- **Overworld:** a dimensão principal, onde o jogo começa.
- **Seed (semente):** número que gera o mundo; a mesma seed gera o mesmo mundo na mesma versão.
- **Snapshot / Preview:** versões de teste da Java e da Bedrock, respectivamente.
- **Spawn:** aparecimento de mobs, ou o ponto onde o jogador nasce.
- **Stack:** pilha de itens; a maioria empilha até 64, alguns até 16 (pérolas, ovos, placas) e outros não empilham (ferramentas, poções).
- **Tick:** unidade de tempo do jogo; 20 ticks = 1 segundo.
- **Vanilla:** o jogo oficial sem mods.
