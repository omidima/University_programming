public class index {
    class Foods {
        private String food;

        public String getfood(int foodNumber) {
            switch (foodNumber) {
            case 1:
                return "omlet";
            case 2:
                return "kabab";
            case 3:
                return "kooft";
            }
            return null;
        }
    }

    class Clothds {
        private String clothds;

        public String getclothds(int clothdsNumber) {
            switch (clothdsNumber) {
            case 1:
                return "T-shirt";
            case 2:
                return "jacket";
            case 3:
                return "sout";
            }
            return null;
        }
    }

    class Shoze {
        private String shoze;

        public String getShoze(int shozeNumber) {
            switch (shozeNumber) {
            case 1:
                return "addidass";
            case 2:
                return "mely";
            case 3:
                return "nike";
            }
            return null;
        }
    }

    class Cars {
        private String car;

        public String getCars(int carNumber) {
            switch (carNumber) {
            case 1:
                return "benz";
            case 2:
                return "pride";
            case 3:
                return "bmw";
            }
            return null;
        }
    }
}