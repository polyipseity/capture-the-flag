public class Main {
  public static void main(String[] args) throws Exception {
    System.setErr(System.out);
    System.out.println("Running...");
    new ProcessBuilder("cat", "flag.txt")
        .inheritIO()
        .start()
        .waitFor();
    /*
     * ProcessBuilder pb = new ProcessBuilder(Arrays.asList("cat",
     * "flag.txt")).redirectErrorStream(true);
     * Process process = pb.start();
     * StringBuilder result = new StringBuilder();
     * try (BufferedReader in = new BufferedReader(new
     * InputStreamReader(process.getInputStream()))) {
     * while (true) {
     * String line = in.readLine();
     * if (line == null)
     * break;
     * result.append(line).append(System.lineSeparator());
     * }
     * }
     * System.out.println(result.toString());
     */
  }
}
