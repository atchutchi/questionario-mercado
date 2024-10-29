// tarifario_voz.js
document.addEventListener('DOMContentLoaded', function() {
    // Seleciona o formulário tanto para Orange quanto MTN
    const form = document.querySelector('form');
    
    // Validação do formulário
    form.addEventListener('submit', function(event) {
        let isValid = true;
        const inputs = form.querySelectorAll('input[type="number"], input[type="text"]');
        
        // Percorre todos os inputs do formulário
        inputs.forEach(function(input) {
            // Remove mensagens de erro anteriores
            removeError(input);
            
            // Validação de campo obrigatório
            if (input.hasAttribute('required') && !input.value) {
                isValid = false;
                showError(input, 'Este campo é obrigatório.');
            }
            
            // Validação de números negativos
            if (input.type === 'number' && parseFloat(input.value) < 0) {
                isValid = false;
                showError(input, 'O valor deve ser maior ou igual a zero.');
            }
 
            // Validação específica para campos de taxa/imposto
            if (input.name.includes('taxa_imposto')) {
                const taxaPattern = /^(TVA\s*19%(\s*\+\s*IET)?|19%)$/;
                if (!taxaPattern.test(input.value)) {
                    isValid = false;
                    showError(input, 'Formato inválido. Use "TVA 19%" ou "TVA 19% + IET"');
                }
            }
 
            // Validação para campos monetários
            if (input.classList.contains('currency-input') && input.value && isNaN(input.value)) {
                isValid = false;
                showError(input, 'Digite apenas números.');
            }
        });
 
        // Validações específicas para Orange
        if (form.classList.contains('orange-form')) {
            // Validação dos pacotes de internet
            const internetPacks = [
                'pass_ilimite_1h', 'pass_ilimite_3h', 'pass_ilimite_8h',
                'pass_30_mo', 'pass_75_mo', 'pass_150_mo'
            ];
            
            internetPacks.forEach(packName => {
                const input = form.querySelector(`[name="${packName}"]`);
                if (input && input.value && parseInt(input.value) <= 0) {
                    isValid = false;
                    showError(input, 'O valor do pacote deve ser maior que zero.');
                }
            });
 
            // Validação das tarifas de chamadas
            const callRates = [
                'tarifa_orange_livre_6h_22h', 'tarifa_orange_livre_22h_6h',
                'tarifa_orange_jovem_vip_jovem'
            ];
            
            callRates.forEach(rateName => {
                const input = form.querySelector(`[name="${rateName}"]`);
                if (input && parseFloat(input.value) < 0) {
                    isValid = false;
                    showError(input, 'A tarifa não pode ser negativa.');
                }
            });
        }
 
        // Validações específicas para MTN
        if (form.classList.contains('mtn-form')) {
            // Validação dos pacotes de dados
            const dataPacks = [
                'pacote_30mb', 'pacote_100mb', 'pacote_300mb',
                'pacote_1gb', 'pacote_650mb', 'pacote_1000mb'
            ];
            
            dataPacks.forEach(packName => {
                const input = form.querySelector(`[name="${packName}"]`);
                if (input && input.value && parseInt(input.value) <= 0) {
                    isValid = false;
                    showError(input, 'O valor do pacote deve ser maior que zero.');
                }
            });
        }
 
        // Impede o envio do formulário se houver erros
        if (!isValid) {
            event.preventDefault();
            // Scroll para o primeiro erro
            const firstError = form.querySelector('.is-invalid');
            if (firstError) {
                firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        }
    });
 
    // Função para mostrar mensagem de erro
    function showError(input, message) {
        input.classList.add('is-invalid');
        const errorDiv = document.createElement('div');
        errorDiv.className = 'invalid-feedback';
        errorDiv.innerText = message;
        input.parentNode.appendChild(errorDiv);
    }
 
    // Função para remover mensagem de erro
    function removeError(input) {
        input.classList.remove('is-invalid');
        const errorDiv = input.parentNode.querySelector('.invalid-feedback');
        if (errorDiv) {
            errorDiv.remove();
        }
    }
 
    // Formatar campos monetários
    const currencyInputs = document.querySelectorAll('.currency-input');
    currencyInputs.forEach(function(input) {
        input.addEventListener('input', function(e) {
            // Remove tudo exceto números e ponto
            let value = this.value.replace(/[^\d.]/g, '');
            
            // Garante apenas um ponto decimal
            const parts = value.split('.');
            if (parts.length > 2) {
                value = parts[0] + '.' + parts.slice(1).join('');
            }
            
            // Limita a 2 casas decimais
            if (parts[1] && parts[1].length > 2) {
                value = parts[0] + '.' + parts[1].slice(0, 2);
            }
            
            this.value = value;
        });
    });
 
    // Atualizar totais automaticamente
    const calculateTotals = function() {
        // Total de Internet Pré-pago
        const prepaidInputs = document.querySelectorAll('[name*="dongle"], [name*="airbox"], [name*="flybox"]');
        const totalPrepaid = Array.from(prepaidInputs)
            .reduce((sum, input) => sum + (parseFloat(input.value) || 0), 0);
        document.getElementById('total-prepaid').textContent = totalPrepaid.toFixed(2);
 
        // Total de Passes
        const passInputs = document.querySelectorAll('[name*="pass_"]');
        const totalPasses = Array.from(passInputs)
            .reduce((sum, input) => sum + (parseFloat(input.value) || 0), 0);
        document.getElementById('total-passes').textContent = totalPasses.toFixed(2);
    };
 
    // Adicionar listeners para atualização automática
    const numericInputs = form.querySelectorAll('input[type="number"]');
    numericInputs.forEach(input => {
        input.addEventListener('input', calculateTotals);
    });
 
    // Calcular totais iniciais
    calculateTotals();
 
    // Limpar campos quando mudar entre Orange e MTN
    const operadoraSelect = document.querySelector('[name="operadora"]');
    if (operadoraSelect) {
        operadoraSelect.addEventListener('change', function() {
            form.reset();
            // Remove todas as mensagens de erro
            document.querySelectorAll('.invalid-feedback').forEach(el => el.remove());
            document.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));
        });
    }
 });