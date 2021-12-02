
  
<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="drf_ihs_markter_es_test_0"></a>drf_ihs_markter_es_test</h1>
<h2 class="code-line" data-line-start=1 data-line-end=2 ><a id="Dmitriy_Smolskiy__1"></a>Dmitriy Smolskiy</h2>
<p class="has-line-data" data-line-start="3" data-line-end="4">Drf+ElasticSearch+Docker-compose</p>
<ol>
<li class="has-line-data" data-line-start="5" data-line-end="6">Запуск два контейнера Django + Elastic</li>
</ol>
<pre><code class="has-line-data" data-line-start="7" data-line-end="9" class="language-sh">Docker-compose up <span class="hljs-operator">-d</span> --build
</code></pre>
<ol start="2">
<li class="has-line-data" data-line-start="10" data-line-end="11">Создаём пользователей и статьи.</li>
</ol>
<pre><code class="has-line-data" data-line-start="12" data-line-end="14" class="language-sh">docker-compose <span class="hljs-built_in">exec</span> web python manage.py create_db 
</code></pre>
<p class="has-line-data" data-line-start="14" data-line-end="15">3.Чтобы создать и заполнить индекс и сопоставление Elasticsearch, используем</p>
<pre><code class="has-line-data" data-line-start="16" data-line-end="18" class="language-sh">docker-compose <span class="hljs-built_in">exec</span> web python manage.py search_index --rebuild  
</code></pre>
<ol start="4">
<li class="has-line-data" data-line-start="18" data-line-end="20">
<p class="has-line-data" data-line-start="18" data-line-end="19"><a href="http://localhost:8000/blog/">http://localhost:8000/blog/</a> - Можно посмотреть все данные в базе данных (без использования elasticsearch)</p>
</li>
<li class="has-line-data" data-line-start="20" data-line-end="21">
<p class="has-line-data" data-line-start="20" data-line-end="21"><a href="http://localhost:8000/search/article/">http://localhost:8000/search/article/</a> - после /  в адресной строке, вставляем запрос по поиску. Имя автора или текст из статьи.</p>
</li>
<li class="has-line-data" data-line-start="21" data-line-end="22">
<p class="has-line-data" data-line-start="21" data-line-end="22"><a href="http://localhost:8000/search/top_authors/">http://localhost:8000/search/top_authors/</a> - выводит топ-10 авторов по количесву публикаций.</p>
</li>
<li class="has-line-data" data-line-start="22" data-line-end="24">
<p class="has-line-data" data-line-start="22" data-line-end="23"><a href="http://localhost:8000/search/search_range_date/">http://localhost:8000/search/search_range_date/</a> - выводит статьи за последние 24 месяца.</p>
</li>
</ol>
