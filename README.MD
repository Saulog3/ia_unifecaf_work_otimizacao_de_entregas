## 🗺️ Diagrama do Grafo
![Grafo de Entregas](static/cluster_plot.png)


## 📈 Análise dos Resultados
- **Clusters**: 3 zonas de entrega otimizadas.
- **Redução de distância**: 30-40% em rotas otimizadas vs. manuais (baseado em testes com dados sintéticos).
- **Tempo de execução**: K-Means (0.1s), A* (0.5s por rota).
- **Limitações**: Dados sintéticos não incluem tráfego real ou obstáculos urbanos.


## 💡 Melhorias Futuras
- Integração com APIs de tráfego em tempo real (Google Maps, Waze).
- Uso de aprendizado por reforço para ajustar rotas dinamicamente.
- Testes com dados reais da Sabor Express para validação.
