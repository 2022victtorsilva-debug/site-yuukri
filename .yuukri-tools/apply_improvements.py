from pathlib import Path

path = Path("index.html")
text = path.read_text(encoding="utf-8")


def replace_once(old, new, label):
    global text
    if old not in text:
        raise SystemExit(f"Trecho não encontrado: {label}")
    text = text.replace(old, new, 1)


replace_once(
'''    .section--soft {
      border-block: 1px solid var(--line);
      background:
        linear-gradient(180deg, rgba(13, 18, 27, 0.58), rgba(7, 10, 15, 0.84));
    }''',
'''    .section--soft {
      background:
        radial-gradient(circle at 82% 18%, rgba(37, 99, 235, 0.055), transparent 24rem),
        linear-gradient(180deg, rgba(13, 18, 27, 0.52), rgba(7, 10, 15, 0.82));
    }''',
"section--soft")

replace_once(
'''    .projects {
      display: grid;
      gap: 24px;
    }''',
'''    .projects {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      align-items: stretch;
      gap: 24px;
    }''',
"projects")

replace_once(
'''    .project {
      display: grid;
      grid-template-columns: 1.45fr 1fr;
      overflow: hidden;''',
'''    .project {
      display: grid;
      grid-template-rows: auto 1fr;
      overflow: hidden;''',
"project layout")

replace_once(
'''    .project:nth-child(even) {
      grid-template-columns: 1fr 1.45fr;
    }

    .project:nth-child(even) .project__image {
      order: 2;
    }

''',
''' ''',
"alternância projetos")

replace_once(
'''    .project__image {
      position: relative;
      display: block;
      height: 390px;''',
'''    .project__image {
      position: relative;
      display: block;
      height: 520px;''',
"altura imagem projeto")

replace_once(
'''    .project__body {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: space-between;
      padding: clamp(28px, 4.4vw, 52px);
    }''',
'''    .project__body {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: space-between;
      gap: 30px;
      min-height: 248px;
      padding: clamp(26px, 3.4vw, 40px);
    }''',
"corpo projeto")

replace_once(
'''      .project,
      .project:nth-child(even) {
        grid-template-columns: 1fr;
      }

      .project:nth-child(even) .project__image {
        order: 0;
      }

      .project__image {
        height: 320px;
      }''',
'''      .projects {
        grid-template-columns: 1fr;
      }

      .project__image {
        height: 440px;
      }''',
"portfolio tablet")

replace_once(
'''      .section {
        padding: 74px 0;
      }''',
'''      .section {
        padding: 68px 0;
      }''',
"espaçamento mobile")

replace_once(
'''      .project__image {
        height: 270px;
      }''',
'''      .project__image {
        height: 380px;
      }''',
"imagem mobile")

replace_once(
'''    .reveal.reveal-pending {
      opacity: 0;
      transform: translateY(18px);
    }''',
'''    .reveal.reveal-pending {
      opacity: 0;
      transform: translateY(22px);
    }''',
"reveal")

amor_marker = '''          <article class="project reveal">
            <a
              class="project__image"
              href="https://2022victtorsilva-debug.github.io/Jo-oVicttorgithub.io./"'''
vittu = '''          <article class="project reveal">
            <a
              class="project__image"
              href="https://2022victtorsilva-debug.github.io/modelo-site-de-loja/"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="Abrir projeto Vittu Lojas em nova aba"
            >
              <img
                src="assets/vittu-lojas-capa.jpg"
                alt="Página inicial do site Vittu Lojas"
                loading="lazy"
              >
              <span class="project__overlay">Ver projeto ↗</span>
            </a>

            <div class="project__body">
              <div>
                <p class="eyebrow">Site para loja</p>
                <h3>Vittu Lojas</h3>

                <p>
                  Site desenvolvido para apresentar uma loja de moda feminina,
                  com coleções, novidades, informações e contato.
                </p>
              </div>

              <a
                href="https://2022victtorsilva-debug.github.io/modelo-site-de-loja/"
                target="_blank"
                rel="noopener noreferrer"
              >
                Ver projeto <span aria-hidden="true">→</span>
                <span class="sr-only">Vittu Lojas (abre em nova aba)</span>
              </a>
            </div>
          </article>

'''
replace_once(amor_marker, vittu + amor_marker, "inserção Vittu")

process_marker = '''          </article>
        </div>
      </div>
    </section>

    <section
      class="section section--soft"
      aria-labelledby="process-title"'''
traco = '''          </article>

          <article class="project reveal">
            <a
              class="project__image"
              href="https://2022victtorsilva-debug.github.io/Site-cria-o-de-quadrinho/"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="Abrir projeto Traço & História em nova aba"
            >
              <img
                src="assets/traco-historia-capa.jpg"
                alt="Página inicial do sistema Traço & História"
                loading="lazy"
              >
              <span class="project__overlay">Ver projeto ↗</span>
            </a>

            <div class="project__body">
              <div>
                <p class="eyebrow">Sistema web</p>
                <h3>Traço &amp; História</h3>

                <p>
                  Aplicação web para criação de desenhos e quadrinhos, com editor
                  interativo, salvamento de projetos e recursos de pesquisa de imagens.
                </p>
              </div>

              <a
                href="https://2022victtorsilva-debug.github.io/Site-cria-o-de-quadrinho/"
                target="_blank"
                rel="noopener noreferrer"
              >
                Ver projeto <span aria-hidden="true">→</span>
                <span class="sr-only">Traço &amp; História (abre em nova aba)</span>
              </a>
            </div>'''
replace_once(process_marker, traco + '''
          </article>
        </div>
      </div>
    </section>

    <section
      class="section section--soft"
      aria-labelledby="process-title"''', "inserção Traço")

reveal_marker = '''    const revealItems =
      document.querySelectorAll(".reveal");'''
stagger = '''    document.querySelectorAll(".benefits, .process").forEach((group) => {
      group.querySelectorAll(".reveal").forEach((item, index) => {
        item.dataset.revealDelay = String(index * 65);
      });
    });

'''
replace_once(reveal_marker, stagger + reveal_marker, "stagger")

replace_once(
'''    if (
      reducedMotion ||
      compactViewport ||
      !("IntersectionObserver" in window)
    ) {''',
'''    if (
      reducedMotion ||
      !("IntersectionObserver" in window)
    ) {''',
"reveal mobile")

replace_once(
'''      const revealItem = (item) => {
        item.classList.remove("reveal-pending");
        item.classList.add("is-visible");
      };''',
'''      const revealItem = (item) => {
        const delay = Number(item.dataset.revealDelay || 0);
        if (delay) item.style.transitionDelay = `${delay}ms`;

        item.classList.remove("reveal-pending");
        item.classList.add("is-visible");

        if (delay) {
          window.setTimeout(() => {
            item.style.transitionDelay = "";
          }, delay + 700);
        }
      };''',
"reveal delay")

path.write_text(text, encoding="utf-8")
