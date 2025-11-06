import java.util.HashMap;
import java.util.HashSet;

public class Principal {
    public static void main(String[] args) {
        HashMap<String, Sessao> sessoes = new HashMap<>();

        Sessao sessao1 = new Sessao("123456789", "Dados da Sessão 1");
        Sessao sessao2 = new Sessao("123456788", "Dados da Sessão 2");
        Sessao sessao3 = new Sessao("987654321", "Dados da Sessão 3");

        sessoes.put(sessao1.numeroCelular, sessao1);
        sessoes.put(sessao2.numeroCelular, sessao2);
        sessoes.put(sessao3.numeroCelular, sessao3);


        String celularBusca = "123456789";

        Sessao sessaoEncontrada = sessoes.get(celularBusca);

        if (sessaoEncontrada != null) {
            System.out.println("Sessão encontrada: " + sessaoEncontrada.dadosSessao);
        } else {
            System.out.println("Sessão não encontrada.");
        }
    }
}
