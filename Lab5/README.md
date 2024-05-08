У вихідному коді стратегії пошуку товарів були реалізовані як класи з методом search_product, який приймав список продуктів та пошуковий запит. Клас ProductManager містив поле для зберігання обраної стратегії, а також методи для виклику цієї стратегії.

У відредагованому коді стратегії пошуку також мають метод search_product, але вони вже не є підкласами ProductSearchStrategy. Замість цього, вони є статичними методами. ProductManager також містить статичні методи search_product та display_products, які викликають методи стратегій безпосередньо, без залежності від конкретних стратегій.

Це дозволяє знизити залежність класу ProductManager від конкретних стратегій, а також робить код більш чистим і зрозумілим, оскільки всі операції здійснюються безпосередньо через статичні методи.