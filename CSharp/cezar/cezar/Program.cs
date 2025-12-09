namespace Cezar
{
    internal static class Program
    {
        private static void Main(string[] argok)
        {
            if (argok.Length == 0)
            {
                RunInteractive();
                return;
            }

            var mod = argok[0].ToLowerInvariant();
            if (mod != "encode" && mod != "decode" && mod != "e" && mod != "d")
            {
                System.Console.WriteLine("Az első argumentumnak 'encode'|'e' vagy 'decode'|'d' kell lennie.");
                return;
            }

            if (argok.Length < 3)
            {
                System.Console.WriteLine("Használat: encode|decode <eltolás> \"szöveg\"");
                return;
            }

            if (!int.TryParse(argok[1], out var eltolas))
            {
                System.Console.WriteLine("Az eltolásnak egész számnak kell lennie.");
                return;
            }

            var szoveg = string.Empty;
            for (var idx = 2; idx < argok.Length; idx++)
            {
                if (idx > 2) szoveg += " ";
                szoveg += argok[idx];
            }

            var eredmeny = CaesarCipher.Shift(szoveg, mod.StartsWith("d") ? -eltolas : eltolas);
            System.Console.WriteLine(eredmeny);
        }

        private static void RunInteractive()
        {
            while (true)
            {
                System.Console.Write("Mód (encode/decode, kilép: exit): ");
                var mod = System.Console.ReadLine()?.Trim().ToLowerInvariant() ?? string.Empty;
                if (mod == "exit" || mod == "kilep" || mod == "q" || mod == "quit")
                {
                    break;
                }

                if (mod != "encode" && mod != "decode" && mod != "e" && mod != "d")
                {
                    System.Console.WriteLine("Érvénytelen mód. Írd be: encode vagy decode (vagy exit a kilépéshez).");
                    continue;
                }

                System.Console.Write("Eltolás (egész szám, kilép: exit): ");
                var eltolasInput = System.Console.ReadLine()?.Trim() ?? string.Empty;
                if (eltolasInput == "exit" || eltolasInput == "kilep" || eltolasInput == "q" || eltolasInput == "quit")
                {
                    break;
                }

                if (!int.TryParse(eltolasInput, out var eltolas))
                {
                    System.Console.WriteLine("Érvénytelen eltolás. Próbáld újra.");
                    continue;
                }

                System.Console.Write("Szöveg (kilép: exit): ");
                var szoveg = System.Console.ReadLine() ?? string.Empty;
                if (szoveg == "exit" || szoveg == "kilep" || szoveg == "q" || szoveg == "quit")
                {
                    break;
                }

                var eredmeny = CaesarCipher.Shift(szoveg, mod.StartsWith("d") ? -eltolas : eltolas);
                System.Console.WriteLine();
                System.Console.WriteLine("Eredmény:");
                System.Console.WriteLine(eredmeny);
                System.Console.WriteLine();
            }
        }
    }

    internal static class CaesarCipher
    {
        public static string Shift(string bemenet, int eltolas)
        {
            if (string.IsNullOrEmpty(bemenet))
            {
                return bemenet;
            }

            var eltolasMod = ((eltolas % 26) + 26) % 26;
            var puffer = new char[bemenet.Length];

            for (var idx = 0; idx < bemenet.Length; idx++)
            {
                var kar = bemenet[idx];
                if (kar >= 'A' && kar <= 'Z')
                {
                    puffer[idx] = (char)('A' + (kar - 'A' + eltolasMod) % 26);
                }
                else if (kar >= 'a' && kar <= 'z')
                {
                    puffer[idx] = (char)('a' + (kar - 'a' + eltolasMod) % 26);
                }
                else
                {
                    puffer[idx] = kar;
                }
            }

            return new string(puffer);
        }
    }
}